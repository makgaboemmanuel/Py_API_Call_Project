import functools # to cache the function executions - the library to use is called: functools
import requests as re

# we need to cache the function executions - the library to use is called: functools
class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api/latest.json"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @functools.lru(maxsize=2) # lru = least recently used, 2 is used because there are no arguments. if there are, increase the cache size
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



