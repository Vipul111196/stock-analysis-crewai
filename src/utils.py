COMPANY_TO_TICKER = {
    "microsoft": "MSFT",
    "apple": "AAPL",
    "amazon": "AMZN",
    "google": "GOOGL",
    "meta": "META",
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "netflix": "NFLX",
    "intel": "INTC",
    "adobe": "ADBE",
    "paypal": "PYPL",
    "salesforce": "CRM",
}


def resolve_ticker(user_input: str) -> str:
    """Resolve a company name or ticker symbol to a valid uppercase ticker."""
    symbol = COMPANY_TO_TICKER.get(user_input.strip().lower(), user_input.strip().upper())
    if not symbol.isalpha() or len(symbol) > 5:
        raise ValueError(f"'{user_input}' is not a valid stock symbol or company name.")
    return symbol
