from kucoin_futures.client import Market

from regex import R

from functions import messageMenu


client = Market(url='https://api-sandbox-futures.kucoin.com')
client = Market(is_sandbox=True)


def getPriceToken(token):
    data = client.get_ticker(token)
    price_int = data['price']

    return float(price_int) 
