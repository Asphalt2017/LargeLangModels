from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str) -> str:
    """
    Lookup a person's LinkedIn profile
    """
    search = TavilySearchResults()
    results = search.run(f"{name}")
    return results[0]["url"]