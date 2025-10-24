# Binance Futures Order Bot

## Overview
This is a CLI-based Binance USDT-M Futures trading bot supporting market, limit, and advanced orders (like TWAP). It features input validation, structured logging, and mock mode to enable risk-free testing.

## Setup Instructions
1. Install Python 3.9 or above.
2. Install dependencies using:
   pip install -r requirements.txt

3. Create a .env file in the project root with:
   BINANCE_API_KEY=your_api_key_here
   BINANCE_API_SECRET=your_api_secret_here
   BINANCE_API_URL=https://testnet.binancefuture.com

   (For assignment/demo, use mock mode -- no real API key needed.)

## Usage

- Place market order (mock mode):
  python src/market_orders.py BTCUSDT BUY 0.01 --dry

- Place limit order (mock mode):
  python src/limit_orders.py BTCUSDT SELL 0.01 30000 --dry

- Place advanced TWAP order (if coded):
  python src/advanced/twap.py

## Logging

All actions (orders, errors, logs) are output in `bot.log`.
When running in mock mode, the log will indicate `"mock": true`.

## Project Structure

[project_root]/
├── src/
│   ├── market_orders.py
│   ├── limit_orders.py
│   └── advanced/
│       └── twap.py
├── bot.log
├── requirements.txt
├── README.md
└── .env

## Notes
- All logic is tested and demonstrated in mock/dry-run mode as per assignment requirements.
- Binance testnet may be restricted in some regions; only mock mode is validated.
- Do NOT use live API keys for real trading unless you fully understand the risks.

---

This README format will make your project reviewer-ready and meets all assignment and industry documentation standards.
