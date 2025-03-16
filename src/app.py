import streamlit as st
from crew import StockAnalysisCrew
import os

# Mapping of common company names to ticker symbols
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
}

st.set_page_config(page_title="AI Stock Analyzer", page_icon="📊")

st.title("📈 AI Stock Analysis with CrewAI")
st.write("Enter a company name or stock ticker to generate an automated investment report.")

user_input = st.text_input("Company Name or Stock Symbol", placeholder="e.g., Tesla or TSLA")

if st.button("Analyze"):
    if not user_input:
        st.warning("⚠️ Please enter a company name or stock symbol.")
    else:
        company_symbol = company_to_ticker.get(user_input.lower(), user_input.upper())

        if not company_symbol.isalpha() or len(company_symbol) > 5:
            st.error(f"'{user_input}' doesn't appear to be a valid stock symbol or company name.")
        else:
            with st.spinner(f"Analyzing stock data for {company_symbol}..."):
                try:
                    # Create and run the crew
                    crew_instance = StockAnalysisCrew(company_symbol=company_symbol)
                    crew = crew_instance.crew()
                    result = crew.kickoff()
                    result_text = str(result)

                    # Save result
                    os.makedirs("output", exist_ok=True)
                    file_path = f"output/{company_symbol}_analysis.txt"
                    with open(file_path, "w") as f:
                        f.write(result_text)

                    # Show output
                    st.success(f"✅ Analysis completed and saved to `{file_path}`")
                    st.subheader(f"📄 Report for {company_symbol}")
                    st.text_area(label="Investment Report", value=result_text, height=400)
                except Exception as e:
                    st.error(f"❌ Something went wrong: {e}")
