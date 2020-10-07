import json
import os

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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
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

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_11(self):
        if os.getenv('stock_11') and os.getenv('stock_11_max') and os.getenv('stock_11_min'):
            stock = os.getenv('stock_11')
            threshold = float(os.getenv('stock_11_min'))
            maxi = float(os.getenv('stock_11_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_12(self):
        if os.getenv('stock_12') and os.getenv('stock_12_max') and os.getenv('stock_12_min'):
            stock = os.getenv('stock_12')
            threshold = float(os.getenv('stock_12_min'))
            maxi = float(os.getenv('stock_12_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_13(self):
        if os.getenv('stock_13') and os.getenv('stock_13_max') and os.getenv('stock_13_min'):
            stock = os.getenv('stock_13')
            threshold = float(os.getenv('stock_13_min'))
            maxi = float(os.getenv('stock_13_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_14(self):
        if os.getenv('stock_14') and os.getenv('stock_14_max') and os.getenv('stock_14_min'):
            stock = os.getenv('stock_14')
            threshold = float(os.getenv('stock_14_min'))
            maxi = float(os.getenv('stock_14_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_15(self):
        if os.getenv('stock_15') and os.getenv('stock_15_max') and os.getenv('stock_15_min'):
            stock = os.getenv('stock_15')
            threshold = float(os.getenv('stock_15_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_16(self):
        if os.getenv('stock_16') and os.getenv('stock_16_max') and os.getenv('stock_16_min'):
            stock = os.getenv('stock_16')
            threshold = float(os.getenv('stock_16_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_17(self):
        if os.getenv('stock_17') and os.getenv('stock_17_max') and os.getenv('stock_17_min'):
            stock = os.getenv('stock_17')
            threshold = float(os.getenv('stock_17_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_18(self):
        if os.getenv('stock_18') and os.getenv('stock_18_max') and os.getenv('stock_18_min'):
            stock = os.getenv('stock_18')
            threshold = float(os.getenv('stock_18_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_19(self):
        if os.getenv('stock_19') and os.getenv('stock_19_max') and os.getenv('stock_19_min'):
            stock = os.getenv('stock_19')
            threshold = float(os.getenv('stock_19_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_20(self):
        if os.getenv('stock_20') and os.getenv('stock_20_max') and os.getenv('stock_20_min'):
            stock = os.getenv('stock_20')
            threshold = float(os.getenv('stock_20_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_21(self):
        if os.getenv('stock_21') and os.getenv('stock_21_max') and os.getenv('stock_21_min'):
            stock = os.getenv('stock_21')
            threshold = float(os.getenv('stock_21_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_22(self):
        if os.getenv('stock_22') and os.getenv('stock_22_max') and os.getenv('stock_22_min'):
            stock = os.getenv('stock_22')
            threshold = float(os.getenv('stock_22_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_23(self):
        if os.getenv('stock_23') and os.getenv('stock_23_max') and os.getenv('stock_23_min'):
            stock = os.getenv('stock_23')
            threshold = float(os.getenv('stock_23_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_24(self):
        if os.getenv('stock_24') and os.getenv('stock_24_max') and os.getenv('stock_24_min'):
            stock = os.getenv('stock_24')
            threshold = float(os.getenv('stock_24_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_

    def stock_25(self):
        if os.getenv('stock_25') and os.getenv('stock_25_max') and os.getenv('stock_25_min'):
            stock = os.getenv('stock_25')
            threshold = float(os.getenv('stock_25_min'))
            maxi = float(os.getenv('stock_15_max'))
            raw_details = rh.get_quote(stock)
            call = raw_details['instrument']
            r = requests.get(call)
            response = r.text
            json_load = json.loads(response)
            stock_name = json_load['simple_name']
            price = round(float(raw_details['last_trade_price']), 2)
            msg = f"The current price of {stock_name} is: ${price}"

            if price < threshold or price > maxi:
                day_data = rh.get_historical_quotes(stock, 'hour', 'day')
                dd = day_data['results'][0]['historicals']
                day_numbers = []
                for close_price in dd:
                    day_numbers.append(round(float(close_price['close_price']), 2))
                if day_numbers:
                    day_list = f"\nToday's change list: {day_numbers}\n"
                else:
                    day_list = '\n'

                week_data = rh.get_historical_quotes(stock, 'day', 'week')
                wd = week_data['results'][0]['historicals']
                week_numbers = []
                for close_price in wd:
                    week_numbers.append(round(float(close_price['close_price']), 2))
                week_list = f"Week's change list: {week_numbers}"

                if price < threshold:
                    message = f'{stock} is currently less than ${threshold}\n{msg}{day_list}{week_list}\n\n'
                    return message
                elif price > maxi:
                    message_ = f'{stock} is currently more than ${maxi}\n{msg}{day_list}{week_list}\n\n'
                    return message_
