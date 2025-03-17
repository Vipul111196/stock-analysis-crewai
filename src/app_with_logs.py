import streamlit as st
from crew import StockAnalysisCrew
import os
import time
import io
import sys

# Mapping of company names to ticker symbols
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

st.set_page_config(page_title="AI Stock Analyzer", page_icon="📊", layout="wide")
st.title("🤖📈 AI Stock Analysis with CrewAI")

st.markdown("Enter a **company name** or **stock ticker** below to generate a detailed investment analysis report.")

user_input = st.text_input("🔍 Company Name or Stock Symbol", placeholder="e.g., Tesla or TSLA")

if st.button("Analyze"):
    if not user_input:
        st.warning("⚠️ Please enter a company name or stock symbol.")
    else:
        company_symbol = company_to_ticker.get(user_input.lower(), user_input.upper())

        if not company_symbol.isalpha() or len(company_symbol) > 5:
            st.error(f"'{user_input}' doesn't appear to be a valid stock symbol or company name.")
        else:
            left_col, right_col = st.columns([2, 1])

            with left_col:
                st.subheader(f"📄 Investment Report for {company_symbol}")
                result_placeholder = st.empty()

            with right_col:
                st.subheader("🖥️ Process Log")
                log_placeholder = st.empty()

            try:
                # Redirect stdout to capture logs
                class StreamCapturer(io.StringIO):
                    def write(self, s):
                        super().write(s)
                        log_placeholder.text(self.getvalue())

                old_stdout = sys.stdout
                sys.stdout = StreamCapturer()

                with st.spinner(f"Analyzing {company_symbol}..."):
                    crew_instance = StockAnalysisCrew(company_symbol=company_symbol)
                    crew = crew_instance.crew()

                    # Kick off and show logs in real-time
                    result = crew.kickoff()
                    result_text = str(result)

                    # Save result to file
                    os.makedirs("output", exist_ok=True)
                    file_path = f"output/{company_symbol}_analysis.txt"
                    with open(file_path, "w") as f:
                        f.write(result_text)

                # Restore stdout
                sys.stdout = old_stdout

                result_placeholder.text_area("✅ Analysis Complete", value=result_text, height=500)
                right_col.success(f"✅ Log complete. Report saved to `{file_path}`")

            except Exception as e:
                sys.stdout = old_stdout
                right_col.error(f"❌ Error occurred: {e}")
