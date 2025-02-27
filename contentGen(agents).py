from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.agents import Tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=["query"],
    template="You're a renowned science fiction writer. {query}"
)

# Initialize the language model
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0)
llm_chain = LLMChain(llm=llm, prompt=prompt)

tools = [
    Tool(
        name='Science Fiction Writer',
        func=llm_chain.run,
        description='Use this tool for generating science fiction stories. Input should be a command about generating specific types of stories.'
    )
]

# Initializing an agent with the tools, the language model, and the type of agent we want to use.
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Testing the agent with the new prompt
response = agent.run("Compose an epic science fiction saga about interstellar explorers")
print(response)
