from flask import Flask, jsonify, request
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests


@app.route('/get_stock_data', methods=['GET'])
def get_stock_data():
    symbol = request.args.get('symbol', 'AAPL')  # Default to AAPL if no symbol is provided
    stock = yf.Ticker(symbol)
    history = stock.history(period="5d")  # Get last 5 days of data

    # Convert data to JSON format
    data = []
    for date, row in history.iterrows():
        data.append({
            "date": date.strftime('%Y-%m-%d'),
            "close": round(row['Close'], 2),
            "Volume": round(row['Volume'], 2)
        })

    return jsonify({"symbol": symbol, "history": data})


@app.route('/predict_stock_price', methods=['GET'])
def predict_stock_price():
    symbol = request.args.get('symbol', 'AAPL')
    stock = yf.Ticker(symbol)
    history = stock.history(period="5d")

    if history.empty:
        return jsonify({"error": "No data available for the given stock symbol"}), 400

    last_close_price = round(stock.history(period="1d")["Close"][-1], 2)

    return jsonify({"symbol": symbol, "predicted_price": last_close_price})


if __name__ == '__main__':
    app.run(debug=True)

