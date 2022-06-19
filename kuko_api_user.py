from kucoin_futures.client import User
from functions import open_Json

JsonDataUser = open_Json('json/api.json', 'r')

api_name = JsonDataUser['api_name']
api_key = JsonDataUser['api_key']
api_secret = JsonDataUser['api_secret']
api_passphrase = JsonDataUser['api_passphrase']

client = User(api_key, api_secret, api_passphrase)

amout_usd = client.get_account_overview()

