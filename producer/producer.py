#Import necessary libraries

import time
import json
import requests
from kafka import KafkaProducer

# Define constants
API_KEY = 'd4jjoi1r01qgcb0tn9p0d4jjoi1r01qgcb0tn9pg'
BASE_URL = 'https://finnhub.io/api/v1/quote'
SYMBOLS = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['host.docker.internal:29092'],
    value_serializer = lambda v: json.dumps(v).encode("utf-8")
)

# Function to fetch stock data
def fetch_stock_data(symbol):
    url = f"{BASE_URL}?symbol={symbol}&token={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        data['symbol'] = symbol
        data["fetched_at"] = int(time.time())
        return data
    
    except (Exception) as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None
    
# Main loop to fetch and send data
while True:
    for symbol in SYMBOLS:
        stock_data = fetch_stock_data(symbol)
        if stock_data:
            producer.send('stock_quotes',value=stock_data)
            print(f"Sent data for {symbol}: {stock_data}")
    time.sleep(10)  # Fetch data every 10 seconds

    