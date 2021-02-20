"""/**
 * Author:  Vignesh Sivanandha Rao
 * Created:   08.19.2020
 *
 **/"""
import os
import time
from datetime import datetime, date

import pytz
import requests
from pyrh.exceptions import InvalidTickerSymbol

from lib.aws_client import AWSClients

start_time = time.time()
current_time = datetime.now(pytz.timezone('US/Central'))
dt_string = current_time.strftime("%A, %B %d, %Y %I:%M %p")

logs = 'https://us-west-2.console.aws.amazon.com/cloudwatch/home#logStream:group=/aws/lambda/skynet'


def market_status():
    url = requests.get('https://www.nasdaqtrader.com/trader.aspx?id=Calendar')
    today = date.today().strftime("%B %d, %Y")
    if today in url.text:
        print(f'{today}: The markets are closed today.')
    else:
        return True


def email_formatter():
    from lib.judgement_day import StockChecker

    email_text = ''

    for _, method in StockChecker.__dict__.items():
        if callable(method):
            try:
                if result := method(None):
                    email_text += result
            except InvalidTickerSymbol:
                print(f'Faced an InvalidTickerSymbol with the Ticker::{os.getenv(method.__name__)}')

    if email_text:
        print(email_text)
        return email_text
    else:
        print('I’ll Be Back...')


def send_email():
    email_data = email_formatter()
    if email_data:
        from lib.emailer import Emailer
        sender_env = AWSClients().sender()
        recipient_env = AWSClients().recipient()
        git = 'https://github.com/thevickypedia/skynet'
        footer_text = "\n----------------------------------------------------------------" \
                      "----------------------------------------\n" \
                      "A price change alert for stocks in your watchlist that has either deceeded the MIN threshold" \
                      " or exceeded the MAX limit value.\n" \
                      "The data is being collected from https://api.robinhood.com," \
                      f"\nFor more information check README.md in {git}"
        sender = f'Skynet <{sender_env}>'
        recipient = [f'{recipient_env}']
        title = f'Skynet Alert as of {dt_string}'
        text = f'Skynet Notification\n\n{email_data}Navigate to check logs: {logs}\n\n{footer_text}'
        Emailer(sender, recipient, title, text)
        return email_data


def send_whatsapp(data, context):
    if market_status():
        if whatsapp_msg := email_formatter():
            from twilio.rest import Client
            whatsapp_send = AWSClients().send()
            whatsapp_receive = AWSClients().receive()
            sid = AWSClients().sid()
            token = AWSClients().token()
            from_number = f"whatsapp:{whatsapp_send}"
            to_number = f"whatsapp:{whatsapp_receive}"
            client = Client(sid, token)
            client.messages.create(body=f'{dt_string}\n\nSkynet Alert\n\n{whatsapp_msg}Log info here\n{logs}',
                                   from_=from_number,
                                   to=to_number)
    print(f"Terminated in {round(float(time.time() - start_time), 2)} seconds")


if __name__ == '__main__':
    send_whatsapp("data", "context")
