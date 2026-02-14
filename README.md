# Binance Spot Testnet Trading Bot (Python CLI)

A modular Python-based trading bot that executes Market and Limit orders using the Binance Spot Testnet API.

Built with structured architecture, CLI interface, environment-based configuration, logging, and validation.
## Project Overview

This application:

- Connects securely to Binance Spot Testnet
- Accepts order parameters via CLI
- Validates user inputs
- Places Market and Limit orders
- Logs API requests and responses
- Displays formatted order summaries

The architecture separates:

- API client layer
- Business logic layer
- Validation layer
- Logging layer
- CLI interface layer

---

## Why Binance Spot Testnet Was Used

The assignment mentioned Binance Futures Testnet (USDT-M).

However, Futures Testnet access may be region-restricted. Due to this limitation, Binance Spot Testnet was used:

Base URL:
https://testnet.binance.vision

The architecture and authentication logic remain identical.  
The system can be adapted to Futures Testnet by modifying the base URL and client module.

---

## Features

- Market Orders (BUY / SELL)
- Limit Orders (BUY / SELL)
- Structured CLI commands
- Input validation
- Logging to file
- Environment-based configuration (.env)
- Rich formatted terminal output

---

binance-futures-bot/
│
├── bot/
│ ├── client.py
│ ├── orders.py
│ ├── validators.py
│ ├── logger_config.py
│
├── logs/
├── cli.py
├── requirements.txt
├── .gitignore
└── README.md



## Setup Instructions

### 1. Clone Repository

git clone https://github.com/YOUR_USERNAME/binance-futures-bot.git
cd binance-futures-bot


### 2. Create Virtual Environment

Windows:

python -m venv venv

venv\Scripts\activate


Mac/Linux:

python -m venv venv

source venv/bin/activate


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Configure API Keys

Create a `.env` file in the root directory:

BINANCE_API_KEY=your_api_key_here

BINANCE_API_SECRET=your_secret_key_here

BINANCE_BASE_URL=https://testnet.binance.vision


API keys can be generated from:
https://testnet.binance.vision

Testnet funds are virtual.

---

## CLI Usage

### View Help

python cli.py --help

python cli.py order --help


---

### Place Market Order

python cli.py order place

--symbol BTCUSDT

--side BUY

--type MARKET

--quantity 0.001


---

### Place Limit Order

python cli.py order place

--symbol BTCUSDT

--side SELL

--type LIMIT

--quantity 0.001

--price 70000


---

## Logging

All API activity is logged in:

logs/app.log


Logs include:

- Timestamp
- 
- Order request details
- 
- API response
- 
- Errors (if any)

---

## Error Handling

The system handles:

- Invalid symbol
- Invalid order type
- Missing price for LIMIT orders
- API errors
- Network failures

Errors are logged and displayed clearly.

---

## Security Notice

Never commit your `.env` file or API keys to GitHub.

Ensure `.gitignore` contains:

.env
venv/
logs/


---

## Summary

This project demonstrates:

- Secure API integration
- Structured CLI design
- Modular architecture
- Proper logging
- Validation and error handling
- Clean project structure

## Project Structure
