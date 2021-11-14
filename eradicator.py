from datetime import datetime, date
from logging import basicConfig, getLogger, INFO
from os import environ, path
from time import perf_counter

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


def market_status():
    """Checks market status and returns True only if markets are open."""
    url = get('https://www.nasdaqtrader.com/trader.aspx?id=Calendar')
    today = date.today().strftime("%B %d, %Y")
    if today in url.text:
        logger.warning(f'{today}: The markets are closed today.')
    else:
        return True


def stock_checker(stock_ticker, stock_max, stock_min):
    """Receives ticker, max and min values and returns the changes on each stock if current price < min or > max."""
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
    email_text = ''
    analyzed = 0
    for n in range(1, 101):
        if (stock_ticker := environ.get(f'stock_{n}')) and (stock_max := environ.get(f'stock_{n}_max')) and \
                (stock_min := environ.get(f'stock_{n}_min')):
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
