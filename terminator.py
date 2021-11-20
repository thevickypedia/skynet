from datetime import date, datetime
from json import load
from json.decoder import JSONDecodeError
from logging import INFO, basicConfig, getLogger
from os import environ, path
from time import perf_counter
from typing import Union

from dotenv import load_dotenv
from gmailconnector.send_sms import Messenger
from pyrh import Robinhood
from pyrh.exceptions import InvalidTickerSymbol
from requests import get

basicConfig(level=INFO, datefmt='%b-%d-%Y %H:%M:%S',
            format='%(asctime)s - %(levelname)s - %(funcName)s - Line: %(lineno)d - %(message)s')
logger = getLogger(__name__)

if path.isfile('.env'):
    load_dotenv(dotenv_path='.env', override=True, verbose=True)

dt_string = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

rh = Robinhood()

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
        log(msg=f'{today}: The markets are closed today.')
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
    raw_details = rh.get_quote(stock_ticker)
    price = round(float(raw_details['last_trade_price']), 2)
    call = raw_details['instrument']
    msg = f"The current price of {get(call).json()['simple_name']} is: ${price}"

    if price < stock_min or price > stock_max:
        day_data = rh.get_historical_quotes(stock_ticker, 'hour', 'day')
        dd = day_data['results'][0]['historicals']
        day_numbers = []
        for close_price in dd:
            day_numbers.append(round(float(close_price['close_price']), 2))
        if day_numbers:
            day_list = f"\nToday's change list: {day_numbers}\n"
        else:
            day_list = '\n'

        week_data = rh.get_historical_quotes(stock_ticker, 'day', 'week')
        wd = week_data['results'][0]['historicals']
        week_numbers = []
        for close_price in wd:
            week_numbers.append(round(float(close_price['close_price']), 2))
        week_list = f"Week's change list: {week_numbers}"

        if price < stock_min:
            message = f'{stock_ticker} is currently less than ${stock_min}\n{msg}{day_list}{week_list}\n\n'
            return message
        elif price > stock_max:
            message_ = f'{stock_ticker} is currently more than ${stock_max}\n{msg}{day_list}{week_list}\n\n'
            return message_


def formatter():
    """Triggers the stock checker and formats the whats app message as needed."""
    rh.login(username=environ.get('robinhood_user'), password=environ.get('robinhood_pass'),
             qr_code=environ.get('robinhood_qr'))

    if not (stocks_dict := file_parser()):
        log(msg='Feed file not found.')
        return

    email_text = ''
    analyzed = 0
    for n in range(1, 7_501):
        if (stock_ticker := stocks_dict.get(f'stock_{n}')) and (stock_max := stocks_dict.get(f'stock_{n}_max')) and \
                (stock_min := stocks_dict.get(f'stock_{n}_min')):
            try:
                # noinspection PyUnboundLocalVariable
                if result := stock_checker(stock_ticker, float(stock_max), float(stock_min)):
                    log(msg=result)
                    email_text += result
                analyzed += 1
            except InvalidTickerSymbol:
                log(msg=f'Faced an InvalidTickerSymbol with the Ticker::{stock_ticker}', err=True)
    log(msg=f'Successfully analyzed {analyzed} stocks.')
    rh.logout()
    return email_text


def monitor():
    """Triggers formatter and sends a whats app notification if there were any bothering changes in price."""
    if market_status():
        if notification := formatter():
            gmail_user = environ.get('gmail_user')
            gmail_pass = environ.get('gmail_pass')
            phone = environ.get('phone')
            notify = Messenger(gmail_user=gmail_user, gmail_pass=gmail_pass, phone_number=phone,
                               subject=f'{dt_string}\nSkynet Alert', message=notification).send_sms()
            if notify.ok:
                log(msg=f'Notification was sent to {phone}')
            else:
                log(msg=f'Failed to send notification to {phone}', err=True)
                log(msg=notify.body, err=True)
        else:
            log(msg='Nothing to report.')
    log(msg=f"Terminated in {round(float(perf_counter()), 2)} seconds\n\n")


if __name__ == '__main__':
    monitor()
