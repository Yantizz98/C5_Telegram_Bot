import json
import requests
from config import keys


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, quote, amount):
        try:
            base_key = keys[base]
        except KeyError:
            raise APIException(f"Currency {base} not found!")

        try:
            quote_key = keys[quote]
        except KeyError:
            raise APIException(f"Currency {quote} not found!")

        if base_key == quote_key:
            raise APIException(f'Not possible to transfer identical currencies {base}!')

        try:
            amount = float(amount.replace(",", "."))
        except ValueError:
            raise APIException(f'Failed to process quantity {amount}!')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={quote_key}&from={base_key}&amount={amount}"
        payload = {}
        headers = {"apikey": "PpXybTjFDFwPJQbtgtNEzznBDeYkohf8"}
        response = requests.get(url, headers=headers, data=payload)
        total_base = json.loads(response.content)['result']
        # print(total_base)
        # # r = requests.get(f"https://api.apilayer.com/exchangerates_data/live?base={base}&symbols={sym}")
        # # resp = json.loads(r.content)
        new_price = float(total_base)
        new_price = round(new_price, 3)
        message = f"Price {amount} {base} in {quote} : {new_price}"
        return message



