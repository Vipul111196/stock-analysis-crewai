from crew import StockAnalysisCrew
import os

# Simple company name to ticker mapping
company_to_ticker = {
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
    # Add more if needed
}

if __name__ == "__main__":
    user_input = input("Enter the company name or stock symbol (e.g., Microsoft, AMZN, Apple): ").strip()

    # Try to map company name to ticker
    company_symbol = company_to_ticker.get(user_input.lower(), user_input.upper())

    # Very simple ticker validation
    if not company_symbol.isalpha() or len(company_symbol) > 5:
        print(f"⚠️ '{user_input}' doesn't appear to be a valid stock symbol or company name.")
        exit()

    # Create and run the crew
    crew_instance = StockAnalysisCrew(company_symbol=company_symbol)
    crew = crew_instance.crew()
    result = crew.kickoff()

    # Convert CrewOutput to string
    result_text = str(result)

    # Save result to output folder
    os.makedirs("output", exist_ok=True)
    file_path = f"output/{company_symbol}_analysis.txt"
    with open(file_path, "w") as f:
        f.write(result_text)

    print(f"\n✅ Analysis for '{company_symbol}' saved to {file_path}")
