from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from tools.calculator_tool import CalculatorTool
from tools.sec_tools import SEC10KTool, SEC10QTool

from crewai_tools import WebsiteSearchTool, ScrapeWebsiteTool, TXTSearchTool
import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(api_key= api_key, model="gpt-4o-mini")

@CrewBase
class StockAnalysisCrew:
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, company_symbol="AMZN"):
        self.company_symbol = company_symbol

    @agent
    def research_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['research_analyst'],
            verbose=True,
            llm=llm,
            tools=[
                ScrapeWebsiteTool(),
                SEC10QTool(self.company_symbol),
                SEC10KTool(self.company_symbol),
            ]
        )

    @agent
    def financial_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_analyst'],
            verbose=True,
            llm=llm,
            tools=[
                ScrapeWebsiteTool(),
                WebsiteSearchTool(),
                CalculatorTool(),
                SEC10QTool(self.company_symbol),
                SEC10KTool(self.company_symbol),
            ]
        )

    @agent
    def investment_advisor_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['investment_advisor'],
            verbose=True,
            llm=llm,
            tools=[
                ScrapeWebsiteTool(),
                WebsiteSearchTool(),
                CalculatorTool(),
            ]
        )

    @task
    def research(self) -> Task:
        return Task(
            config=self.tasks_config['research'],
            agent=self.research_analyst_agent(),
            input={"company_stock": self.company_symbol}
        )

    @task
    def financial_analysis(self) -> Task: 
        return Task(
            config=self.tasks_config['financial_analysis'],
            agent=self.financial_analyst_agent(),
            input={"company_stock": self.company_symbol}
        )

    @task
    def filings_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['filings_analysis'],
            agent=self.financial_analyst_agent(),
            input={"company_stock": self.company_symbol}
        )

    @task
    def recommend(self) -> Task:
        return Task(
            config=self.tasks_config['recommend'],
            agent=self.investment_advisor_agent(),
            input={"company_stock": self.company_symbol}
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
