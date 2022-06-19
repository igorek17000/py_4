from kucoin_futures.client import Market

from regex import R

from functions import messageMenu


client = Market(url='https://api-sandbox-futures.kucoin.com')
client = Market(is_sandbox=True)

priceBTC = client.get_current_mark_price("XBTUSDM")



        
