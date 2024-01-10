import logging
import requests
from bs4 import BeautifulSoup
import requests_cache

logger = logging.getLogger(__name__)


def fetch_neuroscience_articles(term="neuroscience", retmax=20):
    """Fetch recent neuroscience articles from PubMed.
    Returns a list of article links.

    >>> fetch_neuroscience_articles()
    Returns:
    List[str]: A list of article links.

    >>> fetch_neuroscience_articles(retmax=5)
    Returns:
    List[str]: A list of article links. The list will contain 5 links.

    >>> fetch_neuroscience_articles(term="neuroscience", retmax=5)
    Returns:
    List[str]: A list of article links. The list will contain 5 links. The articles will contain the word "neuroscience" in the title or abstract.

    API documentation: https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch
    """
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    # Set parameters
    params = {
        "db": "pubmed",
        "term": term,
        "usehistory": "y",
        # "api_key": api_key,
        "retmax": retmax,
    }

    with requests_cache.enabled(
        "pubmed_cache", backend="filesystem", expire_after=3600
    ):  # Cache for 1 hour
        # Make the request
        response = requests.get(base_url, params=params)

        # print the request URL
        logger.info(response.url)

        # log whether the response was pulled from the cache
        # or was freshly downloaded
        logger.info("Pulled from cache" if response.from_cache else "Fetched from url")  # type: ignore

        if response.status_code == 200:
            # Parse the XML response
            soup = BeautifulSoup(response.content, "xml")
            article_ids = [id.text for id in soup.find_all("Id")]

            # Fetch article details
            article_links = []
            for article_id in article_ids:
                article_url = f"https://pubmed.ncbi.nlm.nih.gov/{article_id}"
                article_links.append(article_url)

            return article_links
        else:
            err_msg = f"Error: {response.status_code}"
            logger.error(err_msg)
            return None


if __name__ == "__main__":
    # Fetch recent neuroscience articles (change parameters as needed)
    recent_articles = fetch_neuroscience_articles(term="neuroscience")

    if recent_articles:
        for article in recent_articles:
            logger.info(article)
    else:
        logger.error("Failed to fetch articles.")
