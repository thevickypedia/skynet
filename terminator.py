from datetime import datetime, date
from os import environ, path
from time import perf_counter

from dotenv import load_dotenv
from pyrh import Robinhood
from pyrh.exceptions import InvalidTickerSymbol
from requests import get

if path.isfile('.env'):
    load_dotenv(dotenv_path='.env', override=True, verbose=True)

dt_string = datetime.now().strftime("%A, %B %d, %Y %I:%M %p")

rh = Robinhood()


def market_status():
    """Checks market status and returns True only if markets are open."""
    url = get('https://www.nasdaqtrader.com/trader.aspx?id=Calendar')
    today = date.today().strftime("%B %d, %Y")
    if today in url.text:
        print(f'{today}: The markets are closed today.')
    else:
        return True


def stock_checker(stock_ticker, stock_max, stock_min):
    """Receives ticker, max and min values and returns the changes on each stock if current price < min or > max."""
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

    email_text = ''
    for n in range(1, 101):
        if (stock_ticker := environ.get(f'stock_{n}')) and (stock_max := environ.get(f'stock_{n}_max')) and \
                (stock_min := environ.get(f'stock_{n}_min')):
            try:
                # noinspection PyUnboundLocalVariable
                if result := stock_checker(stock_ticker, float(stock_max), float(stock_min)):
                    print(result)
                    email_text += result
            except InvalidTickerSymbol:
                print(f'Faced an InvalidTickerSymbol with the Ticker::{stock_ticker}')

    rh.logout()
    return email_text


def monitor():
    """Triggers formatter and sends a whats app notification if there were any bothering changes in price."""
    if market_status():
        if notification := formatter():
            from gmailconnector.send_sms import Messenger
            gmail_user = environ.get('gmail_user')
            gmail_pass = environ.get('gmail_pass')
            phone = environ.get('phone')
            notify = Messenger(gmail_user=gmail_user, gmail_pass=gmail_pass, phone_number=phone,
                               subject=f'{dt_string}\nSkynet Alert', message=notification).send_sms()
            if notify.get('ok'):
                print(f'Notification was sent to {phone}')
            else:
                print(f'Failed to send notification to {phone}')
        else:
            print('I`ll be Back...')
    print(f"Terminated in {round(float(perf_counter()), 2)} seconds")


if __name__ == '__main__':
    monitor()
