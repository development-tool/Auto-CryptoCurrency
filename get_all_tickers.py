from binance.client import Client

api_key="API_KEYをここに記入"
api_secret = "API_SECRET"


client = Client(api_key, api_secret)


prices = client.get_all_tickers()
print(prices)

