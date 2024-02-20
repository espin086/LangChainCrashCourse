from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import load_tools
from langchain.agents import AgentExecutor, create_react_agent
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import OpenAI
from langchain.agents import load_tools


llm = ChatOpenAI()
tools = load_tools(["wikipedia"], llm=llm)


def pet_namer(animal: str, num_names: int, color: str):
    """
    This function uses the ChatOpenAI class to generate pet names based on the animal type, number of names and color.
    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a world class dog namer."),
            (
                "user",
                "I have a new {animal} that has a {color}, give me {num_names} names",
            ),
        ]
    )

    output_parser = StrOutputParser()

    chain = prompt | llm | output_parser

    response = chain.invoke({"animal": animal, "num_names": num_names, "color": color})
    return response


def agent_wikipedia(input: str):
    """
    This function uses the ChatOpenAI class to generate a response based on the input.
    """

    # Get the prompt to use - you can modify this!
    prompt = hub.pull("hwchase17/react")

    # Construct the ReAct agent
    agent = create_react_agent(llm, tools, prompt)
    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    agent_executor.invoke({"input": f"{input}"})
    return None


if __name__ == "__main__":
    print(agent_wikipedia("What is the capital of France?"))
