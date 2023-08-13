import requests
import json
from const import keys

class ConvertionException(Exception):
    pass


class CryptoConvector:
    @staticmethod
    def conver(awl, soap, amount):



        if ',' in amount:
            amount = amount.replace(",", ".")
        if awl == soap:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты "{awl}"')


        try:
            awl_a = keys[awl]

        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту "{awl}"')
        try:
            soap_b = keys[soap]

        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту "{soap}"')


        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать валюту "{amount}"')




        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={awl_a}&tsyms={soap_b}")
        resoult = json.loads(r.content)[soap_b] * float(amount)

        return resoult