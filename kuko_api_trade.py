from kucoin_futures.client import Trade
from kuko_api_user import api_key, api_name, api_passphrase, api_secret

client = Trade(api_key, api_secret, api_passphrase, is_sandbox=True)
