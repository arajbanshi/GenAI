from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from langchain_openai import ChatOpenAI


load_dotenv()

@tool
def search(query: str) -> str:
    """
    Searches the web for the given query and returns the results.
    Args:
        query (str): The search query.
    Returns:
        str: The search results.
    """
    print(f"Searching for: {query}")
    return "Tokyo weather is sunny"


def main():
    print("Hello from agent search course!")

    llm = ChatOpenAI(model="gpt-5")
    tools = [search]

    agent = create_agent(
        model=llm,
        tools=tools
    )

    result = agent.invoke({"messages": [HumanMessage(content="What is the weather in Tokyo?")]})
    print(result)


if __name__ == "__main__":
    main()