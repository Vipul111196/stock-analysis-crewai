import os
from crew import StockAnalysisCrew
from utils import resolve_ticker


if __name__ == "__main__":
    user_input = input("Enter the company name or stock symbol (e.g., Microsoft, AMZN, Apple): ").strip()

    try:
        company_symbol = resolve_ticker(user_input)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)

    crew_instance = StockAnalysisCrew(company_symbol=company_symbol)
    result = crew_instance.crew().kickoff()

    os.makedirs("output", exist_ok=True)
    file_path = f"output/{company_symbol}_analysis.txt"
    with open(file_path, "w") as f:
        f.write(str(result))

    print(f"\nAnalysis for '{company_symbol}' saved to {file_path}")
