import json
import os
import time

import requests
from pyrh import Robinhood

from lib.aws_client import AWSClients

u = AWSClients().user()
p = AWSClients().pass_()
q = AWSClients().qr_code()
rh = Robinhood()
rh.login(username=u, password=p, qr_code=q)


class StockChecker:
    def stock_1(self):
        if os.getenv('stock_1') and os.getenv('stock_1_max') and os.getenv('stock_1_min'):
            stock = os.getenv('stock_1')
            threshold = float(os.getenv('stock_1_min'))
            maxi = float(os.getenv('stock_1_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold:
                message = f'{stock} is currently less than ${threshold}\n\n{msg}\n\n'
                return message
            elif price > maxi:
                message_ = f'{stock} is currently more than ${maxi}\n\n{msg}\n\n'
                return message_


print(StockChecker().stock_1())

print(round(time.perf_counter()))
