import os
import sys
import io
import streamlit as st
from crew import StockAnalysisCrew
from utils import resolve_ticker

st.set_page_config(page_title="AI Stock Analyzer", page_icon="📊", layout="wide")
st.title("AI Stock Analysis with CrewAI")
st.markdown("Enter a **company name** or **stock ticker** to generate a detailed investment analysis report.")

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

        left_col, right_col = st.columns([2, 1])

        with left_col:
            st.subheader(f"Investment Report for {company_symbol}")
            result_placeholder = st.empty()

        with right_col:
            st.subheader("Process Log")
            log_placeholder = st.empty()

        try:
            # Capture stdout to show agent logs in real-time
            class StreamCapturer(io.StringIO):
                def write(self, s):
                    super().write(s)
                    log_placeholder.text(self.getvalue())

            old_stdout = sys.stdout
            sys.stdout = StreamCapturer()

            with st.spinner(f"Analyzing {company_symbol}..."):
                crew_instance = StockAnalysisCrew(company_symbol=company_symbol)
                result = crew_instance.crew().kickoff()
                result_text = str(result)

                os.makedirs("output", exist_ok=True)
                file_path = f"output/{company_symbol}_analysis.txt"
                with open(file_path, "w") as f:
                    f.write(result_text)

            sys.stdout = old_stdout
            result_placeholder.text_area("Analysis Complete", value=result_text, height=500)
            right_col.success(f"Report saved to `{file_path}`")

        except Exception as e:
            sys.stdout = old_stdout
            right_col.error(f"Error: {e}")
