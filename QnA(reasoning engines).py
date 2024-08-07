import os
os.environ["OPENAI_API_KEY"] = "<YOUR-OPENAI-API-KEY>"
os.environ["GOOGLE_API_KEY"] = "<YOUR-GOOGLE-SEARCH-API-KEY>"
os.environ["GOOGLE_CSE_ID"] = "<YOUR-CUSTOM-SEARCH-ENGINE-ID>"

from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI

# Loading the language model to control the agent
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)

# Loading some tools to use. The llm-math tool uses an LLM, so we pass that in.
tools = load_tools(["google-search", "llm-math"], llm=llm)

# Initializing an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Testing the agent
query = "What's the result of 1000 plus the number of goals scored in the soccer world cup in 2018?"
response = agent.run(query)
print(response)

""" 
Let's break down the steps to see how the agent functions as a "reasoning engine":

Query Processing: The agent receives a query: "What's the result of 1000 plus the number of goals scored in the soccer world cup in 2018?” The agent identifies two distinct tasks within this query - finding out the number of goals scored in the 2018 soccer world cup and adding 1000 to such number.
Tool Utilization: The agent uses the "google-search" tool to answer the first part of the query. This is an example of the agent using external tools to gather accurate and relevant information. The agent isn't creating this information; it's pulling the data from an external source.
Information Processing: For the second part of the query, the agent uses the "llm-math" tool to perform a sum reliably. Again, the agent isn't creating new information. Instead, it's processing the data it has gathered.
Synthesis and Response: After gathering and processing the information, the agent synthesizes it into a coherent response that answers the original query.

""""
