# Stock Dashboard API

A simple Flask API that fetches stock data using Yahoo Finance (`yfinance`).

## Features
- Get last 5 days of stock prices
- Predict latest closing price
- CORS enabled for frontend use

## Installation
```sh
git clone https://github.com/YOUR_USERNAME/stock-dashboard-api.git
cd stock-dashboard-api
python -m venv venv && source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## API Endpoints

### Get Stock Data
`GET /get_stock_data?symbol=TSLA`
```json
{
  "symbol": "TSLA",
  "history": [{ "date": "2024-03-01", "close": 212.34, "Volume": 5000000 }]
}
```

### Predict Stock Price
`GET /predict_stock_price?symbol=GOOGL`
```json
{
  "symbol": "GOOGL",
  "predicted_price": 2800.45
}
```

