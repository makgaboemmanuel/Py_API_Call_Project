import requests as re

class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api/latest.json"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    def latest(self):
        return re.get(f"{self.BASE_URL}?app_id={self.app_id}")

    def convert(self, from_amount,from_currency, to_currency):
        rates = self.latest["rates"]
        to_rate = rates[to_currency]

        if from_currency == "USD":
            return from_amount * to_rate
        else:
            from_in_usd = from_amount / rates[from_currency]
            return from_in_usd * to_rate 



