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

    def stock_2(self):
        if os.getenv('stock_2') and os.getenv('stock_2_max') and os.getenv('stock_2_min'):
            stock = os.getenv('stock_2')
            threshold = float(os.getenv('stock_2_min'))
            maxi = float(os.getenv('stock_2_max'))
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

    def stock_3(self):
        if os.getenv('stock_3') and os.getenv('stock_3_max') and os.getenv('stock_3_min'):
            stock = os.getenv('stock_3')
            threshold = float(os.getenv('stock_3_min'))
            maxi = float(os.getenv('stock_3_max'))
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

    def stock_4(self):
        if os.getenv('stock_4') and os.getenv('stock_4_max') and os.getenv('stock_4_min'):
            stock = os.getenv('stock_4')
            threshold = float(os.getenv('stock_4_min'))
            maxi = float(os.getenv('stock_4_max'))
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

    def stock_5(self):
        if os.getenv('stock_5') and os.getenv('stock_5_max') and os.getenv('stock_5_min'):
            stock = os.getenv('stock_5')
            threshold = float(os.getenv('stock_5_min'))
            maxi = float(os.getenv('stock_5_max'))
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

    def stock_6(self):
        if os.getenv('stock_6') and os.getenv('stock_6_max') and os.getenv('stock_6_min'):
            stock = os.getenv('stock_6')
            threshold = float(os.getenv('stock_6_min'))
            maxi = float(os.getenv('stock_6_max'))
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

    def stock_7(self):
        if os.getenv('stock_7') and os.getenv('stock_7_max') and os.getenv('stock_7_min'):
            stock = os.getenv('stock_7')
            threshold = float(os.getenv('stock_7_min'))
            maxi = float(os.getenv('stock_7_max'))
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

    def stock_8(self):
        if os.getenv('stock_8') and os.getenv('stock_8_max') and os.getenv('stock_8_min'):
            stock = os.getenv('stock_8')
            threshold = float(os.getenv('stock_8_min'))
            maxi = float(os.getenv('stock_8_max'))
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

    def stock_9(self):
        if os.getenv('stock_9') and os.getenv('stock_9_max') and os.getenv('stock_9_min'):
            stock = os.getenv('stock_9')
            threshold = float(os.getenv('stock_9_min'))
            maxi = float(os.getenv('stock_9_max'))
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

    def stock_10(self):
        if os.getenv('stock_10') and os.getenv('stock_10_max') and os.getenv('stock_10_min'):
            stock = os.getenv('stock_10')
            threshold = float(os.getenv('stock_10_min'))
            maxi = float(os.getenv('stock_10_max'))
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
print(StockChecker().stock_2())
print(StockChecker().stock_3())
print(StockChecker().stock_4())
print(StockChecker().stock_5())
print(StockChecker().stock_6())
print(StockChecker().stock_7())
print(StockChecker().stock_8())
print(StockChecker().stock_9())
print(StockChecker().stock_10())

print(round(time.perf_counter()))
