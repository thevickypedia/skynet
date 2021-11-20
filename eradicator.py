from datetime import date, datetime
from json import load
from json.decoder import JSONDecodeError
from logging import INFO, basicConfig, getLogger
from os import environ, path
from time import perf_counter
from typing import Union

from dotenv import load_dotenv
from gmailconnector.send_sms import Messenger
from requests import get
from yfinance import Ticker

basicConfig(level=INFO, datefmt='%b-%d-%Y %H:%M:%S',
            format='%(asctime)s - %(levelname)s - %(funcName)s - Line: %(lineno)d - %(message)s')
logger = getLogger(__name__)

if path.isfile('.env'):
    load_dotenv(dotenv_path='.env', override=True, verbose=True)

dt_string = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

ENV = environ.get('CRON', None)


def log(msg: str, err: bool = False) -> None:
    """Logs or prints the message as necessary.

    Args:
        msg: Takes the message to be logged/printed as an argument.
        err: Boolean flag whether or not to use ``logger.error``
    """
    if ENV:
        print(msg)
    else:
        if err:
            logger.error(msg=msg)
        else:
            logger.info(msg=msg)


def market_status():
    """Checks market status and returns True only if markets are open."""
    log(msg=dt_string)
    url = get('https://www.nasdaqtrader.com/trader.aspx?id=Calendar')
    today = date.today().strftime("%B %d, %Y")
    if today in url.text:
        logger.warning(f'{today}: The markets are closed today.')
    else:
        return True


def file_parser(input_file: str = 'stocks.json') -> dict:
    """Reads the input file and loads the file as dictionary.

    Args:
        input_file: Takes the input file name as an argument.

    Returns:
        dict:
        Returns a json blurb.
    """
    if path.isfile(input_file):
        with open(input_file) as stock_file:
            try:
                return load(fp=stock_file)
            except JSONDecodeError:
                log(msg='Unable to load stocks.json.', err=True)


def stock_checker(stock_ticker: str, stock_max: Union[str, int, float], stock_min: Union[str, int, float]) -> str:
    """Checks whether the current price of the stock has increased or decreased.

    Args:
        stock_ticker: Stock ticker value.
        stock_max: Maximum value after which a notification has to be triggered.
        stock_min: Minimum value below which a notification has to be triggered.

    Returns:
        str:
        Configured notification message.
    """
    raw_details = Ticker(ticker=stock_ticker).info
    price = round(float(raw_details['currentPrice']), 2)
    msg = f"The current price of {raw_details.get('longName')} is: ${price}"

    if price < stock_min or price > stock_max:
        day_list = f"\nToday's change list: {[raw_details.get('previousClose'), raw_details.get('open')]}"

        if price < stock_min:
            message = f'{stock_ticker} is currently less than ${stock_min}\n{msg}{day_list}\n\n'
            return message
        elif price > stock_max:
            message_ = f'{stock_ticker} is currently more than ${stock_max}\n{msg}{day_list}\n\n'
            return message_


def formatter():
    """Triggers the stock checker and formats the whats app message as needed."""
    if not (stocks_dict := file_parser()):
        log(msg='Feed file not found.')
        return

    email_text = ''
    analyzed = 0
    for n in range(1, 7_501):
        if (stock_ticker := stocks_dict.get(f'stock_{n}')) and (stock_max := stocks_dict.get(f'stock_{n}_max')) and \
                (stock_min := stocks_dict.get(f'stock_{n}_min')):
            # noinspection PyUnboundLocalVariable
            if result := stock_checker(stock_ticker, float(stock_max), float(stock_min)):
                logger.info(result)
                email_text += result
                analyzed += 1
    logger.info(f'Successfully analyzed {analyzed} stocks.')
    return email_text


def monitor():
    """Triggers formatter and sends a whats app notification if there were any bothering changes in price."""
    if market_status():
        if notification := formatter():
            notify = Messenger(gmail_user=environ.get('gmail_user'), gmail_pass=environ.get('gmail_pass'),
                               phone_number=environ.get('phone'), subject=f'{dt_string}\nSkynet Alert',
                               message=notification).send_sms()
            if notify.ok:
                logger.info(f"Notification was sent to {environ.get('phone')}")
            else:
                logger.error(f"Failed to send notification to {environ.get('phone')}")
                logger.error(notify.json())
        else:
            logger.info('Nothing to report.')
    logger.info(f"Terminated in {round(float(perf_counter()), 2)} seconds")


if __name__ == '__main__':
    monitor()
