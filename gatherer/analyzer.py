import os

import requests
from pyrh import Robinhood
from pyrh.exceptions import InvalidTickerSymbol
from yfinance import Ticker

from gatherer.traces import prefix

rh = Robinhood()


class Analyzer:
    """Initiates ``Analyzer`` object to instantiate the class methods ``robinhood`` and ``yfinance`` using their API.

    >>> Analyzer

    """

    @classmethod
    def robinhood(cls, stock_ticker: str, stock_max: float, stock_min: float, short: bool = True) -> list:
        """Checks whether the current price of the stock has increased or decreased.

        Args:
            stock_ticker: Stock ticker value.
            stock_max: Maximum value after which a notification has to be triggered.
            stock_min: Minimum value below which a notification has to be triggered.
            short: Boolean flag to send a short summary vs long description.

        Returns:
            list:
            A list of configured notification message and the price.
        """
        raw_details = rh.get_quote(stock_ticker)
        price = round(float(raw_details['last_trade_price']), 2)

        if price < stock_min or price > stock_max:
            if short:
                if price < stock_min:
                    return [f'{stock_ticker} [${price}] is less than {int(stock_min)}\n', price]
                elif price > stock_max:
                    return [f'{stock_ticker} [${price}] is more than ${int(stock_max)}\n', price]

            day_list, week_list = '', ''

            msg = f"Current price of {requests.get(raw_details['instrument']).json()['simple_name']}: ${price}"
            day_data = rh.get_historical_quotes(stock_ticker, 'hour', 'day')
            if day_numbers := [round(float(close_price['close_price']), 2) for close_price in
                               day_data['results'][0]['historicals']]:
                day_list = f"Today's change: {day_numbers}"

            week_data = rh.get_historical_quotes(stock_ticker, 'day', 'week')
            if week_numbers := [round(float(close_price['close_price']), 2) for close_price in
                                week_data['results'][0]['historicals']]:
                week_list = f"Week's change: {week_numbers}"

            if price < stock_min:
                return [f'{stock_ticker} is less than ${stock_min}\n{msg}\n{day_list}\n{week_list}\n', price]
            elif price > stock_max:
                return [f'{stock_ticker} is more than ${stock_max}\n{msg}\n{day_list}\n{week_list}\n', price]

    @classmethod
    def yfinance(cls, stock_ticker: str, stock_max: float, stock_min: float, short: bool = True) -> list:
        """Checks whether the current price of the stock has increased or decreased.

        Args:
            stock_ticker: Stock ticker value.
            stock_max: Maximum value after which a notification has to be triggered.
            stock_min: Minimum value below which a notification has to be triggered.
            short: Boolean flag to send a short summary vs long description.

        Returns:
            list:
            A list of configured notification message and the price.
        """
        raw_details = Ticker(ticker=stock_ticker).info
        price = round(float(raw_details['currentPrice']), 2)

        if price < stock_min or price > stock_max:
            if short:
                if price < stock_min:
                    return [f'{stock_ticker} [${price}] is currently less than {int(stock_min)}\n', price]
                elif price > stock_max:
                    return [f'{stock_ticker} [${price}] is currently more than {int(stock_max)}\n', price]

            msg = f"The current price of {raw_details.get('longName')} is: ${price}"
            day_list = f"\nToday's change list: {[raw_details.get('previousClose'), raw_details.get('open')]}"

            if price < stock_min:
                return [f'{stock_ticker} is currently less than ${stock_min}\n{msg}{day_list}', price]
            elif price > stock_max:
                return [f'{stock_ticker} is currently more than ${stock_max}\n{msg}{day_list}', price]

    @classmethod
    def formatter(cls, stocks_dict: dict) -> dict:
        """Triggers the stock checker and formats the SMS into a dictionary.

        Returns:
            dict:
            Returns a dictionary of ``{stock_ticker: [SMS_text, price]}``
        """
        if (rh_user := os.environ.get('robinhood_user')) and \
                (rh_pass := os.environ.get('robinhood_pass')) and \
                (rh_qr := os.environ.get('robinhood_qr')):
            # noinspection PyUnboundLocalVariable
            rh.login(username=rh_user, password=rh_pass, qr_code=rh_qr)
            print(f"\033[32m{prefix(level='INFO')}Using Robinhood's secure session to monitor watchlist.\033[00m")
            source = cls.robinhood
        else:
            print(f"\033[32m{prefix(level='INFO')}Using YFinance open session to monitor watchlist.\033[00m")
            source = cls.yfinance

        data_dict = {}
        for key, value in stocks_dict.items():
            if len(value) < 2:
                continue
            if isinstance(value, list):
                value = [s for s in value if isinstance(s, int) or isinstance(s, float) or s.isdigit()]
            if isinstance(value, str):
                value = [v.strip() for v in value.split(',') if v.strip().isdigit()]
            try:
                if result := source(stock_ticker=key, stock_max=float(max(value)), stock_min=float(min(value))):
                    data_dict[key] = result
            except InvalidTickerSymbol:
                print(f"\033[31m{prefix(level='ERROR')}"
                      f"Faced an InvalidTickerSymbol with the Ticker::{key}\033[00m")

        if rh.auth_token:
            rh.logout()

        return data_dict
