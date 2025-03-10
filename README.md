# 📈 Stock Analysis with AI Agents using CrewAI 🚀

This project demonstrates how to build a collaborative AI agent system to generate stock investment reports using [CrewAI](https://github.com/joaomdmoura/crewAI). It utilizes a team of AI agents — a Research Analyst, Financial Analyst, and Investment Advisor — who work together to analyze financial data, regulatory filings, and market sentiment to provide actionable investment insights.

## 🧠 Agents Overview

The Crew includes three specialized agents:

- **Research Analyst**  
  Gathers background information, news, and insights about the selected company.

- **Financial Analyst**  
  Analyzes financial statements such as 10-Q filings and compares performance with competitors.

- **Investment Advisor**  
  Compiles all findings into an investment recommendation report.

Each agent has its own role, backstory, and tools, and can delegate tasks and communicate with other agents to enhance analysis quality.

## 🛠️ Features

- ✅ Built with CrewAI
- ✅ Custom AI agents with specific goals and tools
- ✅ Multi-agent collaboration and task delegation
- ✅ Retrieval-Augmented Generation (RAG) system for 10-Q filing analysis
- ✅ Generates a detailed stock investment report
- ✅ Input via stock ticker or company name (e.g., "TSLA" or "Tesla")

## 📊 Example Output

The final report includes:

- Company financial health
- Revenue, profitability, and geographic performance
- Market sentiment and regulatory risks
- Competitive analysis
- Insider trading activity
- Upcoming events (e.g., earnings calls)
- Final investment recommendation

## 🚀 How to Run

1. Clone the repository
2. Install dependencies
3. Run the main script
4. Enter the stock ticker or company name when prompted

```bash
$ git clone https://github.com/Vipul111196/stock-analysis-crewai.git
$ cd stock-analysis-crewai
$ pip install -r requirements.txt
$ python src/main.py
```

## 📂 Tech Stack

- Python 🐍
- CrewAI 🚣
- LangChain 🔗
- OpenAI  🧠
- Financial document parsing (SEC 10-Q)
- Basic RAG setup for document embedding & retrieval

## 📌 Future Improvements Planned

- Add UI for non-technical users
- Expand data sources beyond 10-Q
- More sophisticated competitor analysis
- Add vector database for persistent RAG
- Report export as PDF or HTML

## 📄 License

MIT License


