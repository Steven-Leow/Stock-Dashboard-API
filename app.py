from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from dotenv import load_dotenv
import os


app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

load_dotenv()  # Load from .env
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = "https://www.alphavantage.co/query"


def get_stock_data(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()


@app.route('/stock', methods=['GET'])
def stock():
    symbol = request.args.get("symbol", "AAPL")  # Default to AAPL if not provided
    interval = request.args.get("interval", "5min")
    data = get_stock_data(symbol, interval)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

