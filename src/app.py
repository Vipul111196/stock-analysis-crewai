import os
import streamlit as st
from crew import StockAnalysisCrew
from utils import resolve_ticker

st.set_page_config(page_title="AI Stock Analyzer", page_icon="📊")
st.title("AI Stock Analysis with CrewAI")
st.write("Enter a company name or stock ticker to generate an automated investment report.")

user_input = st.text_input("Company Name or Stock Symbol", placeholder="e.g., Tesla or TSLA")

if st.button("Analyze"):
    if not user_input:
        st.warning("Please enter a company name or stock symbol.")
    else:
        try:
            company_symbol = resolve_ticker(user_input)
        except ValueError as e:
            st.error(str(e))
            st.stop()

        with st.spinner(f"Analyzing stock data for {company_symbol}..."):
            crew_instance = StockAnalysisCrew(company_symbol=company_symbol)
            result = crew_instance.crew().kickoff()
            result_text = str(result)

            os.makedirs("output", exist_ok=True)
            file_path = f"output/{company_symbol}_analysis.txt"
            with open(file_path, "w") as f:
                f.write(result_text)

            st.success(f"Analysis completed and saved to `{file_path}`")
            st.subheader(f"Report for {company_symbol}")
            st.text_area(label="Investment Report", value=result_text, height=400)
