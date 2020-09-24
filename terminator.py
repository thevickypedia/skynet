"""/**
 * Author:  Vignesh Sivanandha Rao
 * Created:   08.19.2020
 *
 **/"""
from datetime import datetime, timedelta, date
import time
import requests

from lib.aws_client import AWSClients
start_time = time.time()
current_time = datetime.now()
utc_to_cdt = current_time - timedelta(hours=5)
dt_string = utc_to_cdt.strftime("%A, %B %d, %Y %I:%M %p")

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
    stock_1_info = StockChecker().stock_1()
    stock_2_info = StockChecker().stock_2()
    stock_3_info = StockChecker().stock_3()
    stock_4_info = StockChecker().stock_4()
    stock_5_info = StockChecker().stock_5()
    stock_6_info = StockChecker().stock_6()
    stock_7_info = StockChecker().stock_7()
    stock_8_info = StockChecker().stock_8()
    stock_9_info = StockChecker().stock_9()
    stock_10_info = StockChecker().stock_10()
    stock_11_info = StockChecker().stock_11()
    stock_12_info = StockChecker().stock_12()
    stock_13_info = StockChecker().stock_13()
    stock_14_info = StockChecker().stock_14()
    stock_15_info = StockChecker().stock_15()
    stock_16_info = StockChecker().stock_16()
    stock_17_info = StockChecker().stock_17()
    stock_18_info = StockChecker().stock_18()
    stock_19_info = StockChecker().stock_19()
    stock_20_info = StockChecker().stock_20()
    stock_21_info = StockChecker().stock_21()
    stock_22_info = StockChecker().stock_22()
    stock_23_info = StockChecker().stock_23()
    stock_24_info = StockChecker().stock_24()
    stock_25_info = StockChecker().stock_25()

    email_text = ''

    if stock_1_info:
        email_text += stock_1_info

    if stock_2_info:
        email_text += stock_2_info

    if stock_3_info:
        email_text += stock_3_info

    if stock_4_info:
        email_text += stock_4_info

    if stock_5_info:
        email_text += stock_5_info

    if stock_6_info:
        email_text += stock_6_info

    if stock_7_info:
        email_text += stock_7_info

    if stock_8_info:
        email_text += stock_8_info

    if stock_9_info:
        email_text += stock_9_info

    if stock_10_info:
        email_text += stock_10_info

    if stock_11_info:
        email_text += stock_11_info

    if stock_12_info:
        email_text += stock_12_info

    if stock_13_info:
        email_text += stock_13_info

    if stock_14_info:
        email_text += stock_14_info

    if stock_15_info:
        email_text += stock_15_info

    if stock_16_info:
        email_text += stock_16_info

    if stock_17_info:
        email_text += stock_17_info

    if stock_18_info:
        email_text += stock_18_info

    if stock_19_info:
        email_text += stock_19_info

    if stock_20_info:
        email_text += stock_20_info

    if stock_21_info:
        email_text += stock_21_info

    if stock_22_info:
        email_text += stock_22_info

    if stock_23_info:
        email_text += stock_23_info

    if stock_24_info:
        email_text += stock_24_info

    if stock_25_info:
        email_text += stock_25_info

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
        whatsapp_msg = email_formatter()
        if whatsapp_msg:
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
