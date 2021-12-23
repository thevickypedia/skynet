from datetime import date, datetime
from json import load
from json.decoder import JSONDecodeError
from os import environ, path
from time import perf_counter, time

import yaml
from boto3 import client
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from gmailconnector.send_sms import Messenger
from requests import get

from gatherer.analyzer import Analyzer
from gatherer.traces import prefix

load_dotenv(dotenv_path='.env', override=True, verbose=True)

dt_string = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

analyze = Analyzer()


def market_status() -> bool:
    """Checks market status and returns True only if markets are open.

    Returns:
        bool:
        True if markets are open on the current date.
    """
    print(f"\033[32m{prefix(level='INFO')}{dt_string}\033[00m")
    url = get('https://www.nasdaqtrader.com/trader.aspx?id=Calendar')
    today = date.today().strftime("%B %d, %Y")
    if today in url.text:
        print(f"\033[2;33m{prefix(level='WARNING')}{today}: The markets are closed today.\033[00m")
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
                print(f"\033[31m{prefix(level='ERROR')}Unable to load stocks.json.\033[00m")


def get_change(current: float, previous: float) -> float:
    """Calculates the percentage change between the current value and previous value.

    Args:
        current: Current price of stock.
        previous: Previous price of stock.

    Returns:
        float:
        Returns the difference percentage.
    """
    if current == previous:
        return 0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return float('inf')


def write_previous(data: dict) -> None:
    """Writes the data received into a yaml file.

    Args:
        data: Data to be written into yaml.
    """
    with open('previous.yaml', 'w') as file:
        yaml.dump(data={"stocks": {k: v[-1] for k, v in data.items()}, "session": time()}, stream=file)


def should_i_notify() -> dict:
    """Looks for the feed file and triggers the analyzer if feed is present.

    See Also:
        Checks the data written in ``previous.yaml`` file and compares the % difference with current price.
        If the difference is less than 5% or no difference at all, returns an empty dict.

    Returns:
        dict:
        Dictionary of the tickers and the price as key value pairs.
    """
    if not (stocks_dict := file_parser()):
        print(f"\033[31m{prefix(level='ERROR')}Feed file not found.\033[00m")
        return {}

    if notification := analyze.formatter(stocks_dict):
        if path.isfile('previous.yaml'):
            with open('previous.yaml') as file:
                previous = yaml.load(stream=file, Loader=yaml.FullLoader)
            remove = []
            for ticker, price in notification.items():
                if prev_price := previous.get('stocks', {}).get(ticker):
                    if get_change(current=price[1], previous=prev_price) < 5 and time() - previous['session'] < 1_800:
                        remove.append(ticker)
            if remove:
                msg = f"No considerable changes on {', '.join(remove)}. Suppressing notifications to reduce noise."
                print(f"\033[32m{prefix(level='INFO')}{msg}\033[00m")
                for tick in remove:
                    notification.pop(tick)
            else:
                write_previous(data=notification)
        else:
            write_previous(data=notification)

        return notification


def aws_sns(phone: str, text: str) -> None:
    """Triggers an SMS notification via AWS SimpleNotificationService.

    Args:
        phone: Phone number of the recipient.
        text: Text which has to be sent.
    """
    try:
        response = client('sns').publish(PhoneNumber=phone,
                                         Subject=f'Skynet Alert - {dt_string}',
                                         Message=text)
        if response.get('ResponseMetadata', {}).get('HTTPStatusCode', 400) == 200:
            print(f"\033[32m{prefix(level='INFO')}Notification was sent to {phone}\n"
                  f"{response.get('ResponseMetadata')}\n\033[00m")
    except ClientError:
        print(f"\033[31m{prefix(level='ERROR')}Failed to send notification to {phone}\033[00m")


def notify(phone: str, text: str) -> None:
    """Triggers notification using gmail-connector which uses the SMS gateway of the carrier.

    Args:
        phone: Phone number of the recipient.
        text: Text which has to be sent.
    """
    notification = Messenger(gmail_user=environ.get('gmail_user'), gmail_pass=environ.get('gmail_pass'),
                             phone=phone, subject=f'{dt_string}\nSkynet Alert', message=text).send_sms()
    if notification.ok:
        print(f"\033[32m{prefix(level='INFO')}Notification was sent to {phone}\033[00m")
    else:
        print(f"\033[31m{prefix(level='ERROR')}Failed to send notification to {phone}\033[00m")
        print(f"\033[31m{prefix(level='ERROR')}{notification.body}\033[00m")
        print(f"\033[2;33m{prefix(level='WARNING')}Initiating notification via AWS SNS.\033[00m")
        aws_sns(text=text, phone=phone)


def monitor():
    """Triggers formatter and sends an SMS notification if there were any bothering changes in price."""
    if not market_status():
        return
    if notification := should_i_notify():
        text = ''
        for n in notification:
            text += notification[n][0]
        text = text.rstrip()
        phone = environ.get('phone')
        if ',' in phone:
            phone = phone.split(',')
        if isinstance(phone, list):
            for each in phone:
                notify(text=text, phone=each.strip())
        else:
            notify(text=text, phone=phone)
    else:
        print(f"\033[32m{prefix(level='INFO')}Nothing to report.\033[00m")
    print(f"\033[32m{prefix(level='INFO')}Terminated in {round(float(perf_counter()), 2)} seconds.\033[00m")


if __name__ == '__main__':
    monitor()
