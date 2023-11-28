import time # to deal with time variables
from openexchange import OpenExchangeClient

import requests as re
start = time.time()  # beginning of aoplication
APP_ID = ""
END_POINT = "https://openexchangerates.org/api/latest.json"

response = re.get(f"{END_POINT}?app_id={APP_ID}")
exchange_rates = response.json()["rates"]
print(exchange_rates)

usd_amount = 1000
gbp_amount = usd_amount * exchange_rates["GBP"]

print(f"USD: {usd_amount} = GBP: {gbp_amount}")
end = time.time()  # end of aoplication
# using the time library
print("using the time library")
print(end -start)





