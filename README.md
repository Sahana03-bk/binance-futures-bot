# binance-futures-bot
# binance-futures-bot
Production-ready Binance Futures Testnet trading bot built with Python, featuring CLI interface, environment-based configuration, logging, validation, and modular architecture.

Binance Testnet Trading Bot (Python CLI)

A modular Python-based trading bot that executes Market and Limit orders using the Binance Spot Testnet API.

Built with structured architecture, CLI interface, environment-based configuration, logging, and validation.

Project Overview

This project implements a command-line trading application that:

Connects securely to Binance Testnet

Accepts user input via CLI

Validates order parameters

Places Market and Limit orders

Logs API requests and responses

Displays formatted order summaries

The application follows a modular architecture separating:

API client layer

Business logic layer

Validation layer

Logging layer

CLI interface layer

Important Note on Exchange Selection

The assignment mentions Binance Futures Testnet (USDT-M).

However, the Futures Testnet interface may be region-restricted or unavailable in certain locations. Due to this limitation, the implementation uses:

Binance Spot Testnet
Base URL:

https://testnet.binance.vision


The architecture and API interaction logic remain identical in structure:

Authenticated requests

HMAC-SHA256 signature

Order placement endpoints

Error handling

Logging

Only the endpoint type differs (Spot vs Futures).
The design is fully extensible to Futures Testnet by changing the base URL and client module.

Features

Market Orders (BUY / SELL)

Limit Orders (BUY / SELL)

Structured CLI commands

Input validation

Logging to file

Environment-based configuration (.env)

Rich formatted terminal output

Modular, reusable architecture

Project Structure
binance_futures_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│
├── logs/                  # Application logs
│
├── cli.py                 # CLI entry point
├── .env                   # Environment variables (not committed)
├── .gitignore
├── requirements.txt
└── README.md

Setup Instructions
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/binance-futures-bot.git
cd binance-futures-bot

2. Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure API Keys

Create a .env file in the root directory:

BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
BINANCE_BASE_URL=https://testnet.binance.vision


API keys can be generated from:
https://testnet.binance.vision

Testnet funds are virtual and automatically provided.

CLI Usage

The application uses a structured CLI built with Typer.

View Help
python cli.py --help

python cli.py order --help

Place Market Order
python cli.py order place \
    --symbol BTCUSDT \
    --side BUY \
    --type MARKET \
    --quantity 0.001

Place Limit Order
python cli.py order place \
    --symbol BTCUSDT \
    --side SELL \
    --type LIMIT \
    --quantity 0.001 \
    --price 70000

What the Application Does Internally

Loads API credentials from environment variables

Initializes Binance client

Validates user inputs

Constructs authenticated request

Sends order to Binance Testnet

Logs request and response

Displays formatted order summary

Logging

All API activity is logged in:

logs/app.log


Each log entry includes:

Timestamp

Order request details

API response

Error messages (if any)

Error Handling

The system handles:

Invalid symbol

Invalid order type

Missing price for LIMIT orders

API response errors

Network failures

Improper CLI usage

Errors are logged and displayed clearly.

Assumptions

Spot Testnet used due to Futures Testnet accessibility constraints

Testnet funds are virtual

Only Market and Limit orders implemented as required

No real trading or financial risk involved

Extensibility

The architecture allows easy extension to:

Binance Futures Testnet

Stop-Limit orders

OCO orders

Account balance commands

Open orders listing

Strategy automation

Web-based interface
