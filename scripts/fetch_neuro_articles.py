import requests
from bs4 import BeautifulSoup
import requests_cache


def fetch_neuroscience_articles(term="neuroscience"):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    # Set parameters
    params = {
        "db": "pubmed",
        "term": term,
        "usehistory": "y",
        # "api_key": api_key,
    }

    with requests_cache.enabled(
        "pubmed_cache", backend="filesystem", expire_after=3600
    ):  # Cache for 1 hour
        # Make the request
        response = requests.get(base_url, params=params)

        # print the request URL
        print(response.url)

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
            print(f"Error: {response.status_code}")
            return None


if __name__ == "__main__":
    # Fetch recent neuroscience articles (change parameters as needed)
    recent_articles = fetch_neuroscience_articles(term="neuroscience")

    if recent_articles:
        for article in recent_articles:
            print(article)
    else:
        print("Failed to fetch articles.")
