import os
from dotenv import load_dotenv
from binance.spot import Spot

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def get_client():
    client = Spot(
        api_key=API_KEY,
        api_secret=API_SECRET,
        base_url="https://testnet.binance.vision"
    )
    return client
