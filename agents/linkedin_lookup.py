import os

from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.tools import get_profile_url_tavily


def lookup(name : str ) -> str:
    """
    Lookup a person's LinkedIn profile
    """
    # Load the API key from the environment
    
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo"
    )
    
    template = """given the full name {name}, 
        I want you to get me a link to their LinkedIn profile. 
        Answer should be a URL only."""
    
    prompt_template = PromptTemplate(
        template=template, input_variables=["name"]
    )

    tools_for_agent = [
        Tool(
            name="linkedin_lookup",
            func=get_profile_url_tavily,
            description="Lookup a person's LinkedIn profile url"
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name=name)}
    )

    linkedin_url = result["output"]
    return linkedin_url

if __name__ == "__main__":
    linkdin_url = lookup("Roudra Saha")
    print(linkdin_url)