
import json

from kucoin_futures.client import Market
client = Market(url='https://api-sandbox-futures.kucoin.com')
client = Market(is_sandbox=True)

log_data = json.load(open('json/log_data.json', 'r', ))

api_key = log_data["api_key"]
api_secret = log_data["api_secret"]
api_passphrase = log_data["api_password"]






