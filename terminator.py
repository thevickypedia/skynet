"""/**
 * Author:  Vignesh Sivanandha Rao
 * Created:   08.19.2020
 *
 **/"""
import json
import os
import time
from datetime import datetime, date

import pytz
import requests
from pyrh.exceptions import InvalidTickerSymbol
from pyrh import Robinhood

from aws_client import AWSClients

current_time = datetime.now(pytz.timezone('US/Central'))
dt_string = current_time.strftime("%A, %B %d, %Y %I:%M %p")

logs = 'https://us-west-2.console.aws.amazon.com/cloudwatch/home#logStream:group=/aws/lambda/skynet'

rh = Robinhood()


def market_status():
    """Checks market status and returns True only if markets are open."""
    url = requests.get('https://www.nasdaqtrader.com/trader.aspx?id=Calendar')
    today = date.today().strftime("%B %d, %Y")
    if today in url.text:
        print(f'{today}: The markets are closed today.')
    else:
        return True


def stock_checker(stock_ticker, stock_max, stock_min):
    """Receives ticker, max and min values and returns the changes on each stock if current price < min or > max."""
    raw_details = rh.get_quote(stock_ticker)
    call = raw_details['instrument']
    r = requests.get(call)
    response = r.text
    json_load = json.loads(response)
    stock_name = json_load['simple_name']
    price = round(float(raw_details['last_trade_price']), 2)
    msg = f"The current price of {stock_name} is: ${price}"

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
    robinhood_user = AWSClients().robinhood_user()
    robinhood_pass = AWSClients().robinhood_pass()
    robinhood_qr = AWSClients().robinhood_qr()
    rh.login(username=robinhood_user, password=robinhood_pass, qr_code=robinhood_qr)

    email_text = ''
    for n in range(1, 101):
        if (stock_ticker := os.getenv(f'stock_{n}')) and (stock_max := os.getenv(f'stock_{n}_max')) and \
                (stock_min := os.getenv(f'stock_{n}_min')):
            try:
                # noinspection PyUnboundLocalVariable
                if result := stock_checker(stock_ticker, float(stock_max), float(stock_min)):
                    email_text += result
            except InvalidTickerSymbol:
                print(f'Faced an InvalidTickerSymbol with the Ticker::{stock_ticker}')

    rh.logout()

    if email_text:
        print(email_text)
        return f'{dt_string}\n\nSkynet Alert\n\n{email_text}Log info here\n{logs}'
    else:
        print('I’ll Be Back...')


def send_whatsapp(data, context):
    """Triggers formatter and sends a whats app notification if there were any bothering changes in price."""
    if market_status():
        if whatsapp_msg := formatter():
            from twilio.rest import Client
            whatsapp_send = AWSClients().send()
            whatsapp_receive = AWSClients().receive()
            sid = AWSClients().sid()
            token = AWSClients().token()
            from_number = f"whatsapp:{whatsapp_send}"
            to_number = f"whatsapp:{whatsapp_receive}"
            client = Client(sid, token)
            client.messages.create(body=whatsapp_msg, from_=from_number, to=to_number)
    print(f"Terminated in {round(float(time.perf_counter()), 2)} seconds")


if __name__ == '__main__':
    send_whatsapp("data", "context")
