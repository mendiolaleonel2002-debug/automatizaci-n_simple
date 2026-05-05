import yfinance as yf
from utils.sanitizar import sanitizar

# Diccionario con las empresas y sus acciones
COMPANY_TICKERS = {
    "apple": "AAPL",
    "microsoft": "MSFT",
    "google": "GOOGL",
    "amazon": "AMZN",
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "meta": "META",
}

def obtener_precio_accion(user_input, ):
    ticker = COMPANY_TICKERS.get(company_name)

    company_name = sanitizar(user_input)