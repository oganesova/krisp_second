import feedparser
import logging
from typing import List

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_headlines(rss_url: str) -> List[str]:
    """
    Extracts article titles from the RSS feed at the specified URL.

    :param rss_url: URL of the RSS feed.
    :return: A list of strings representing the article titles.
    :raises ValueError: If the URL is not a valid RSS resource or if there are issues parsing it.
    """
    try:
        logging.info(f"Parsing RSS feed from URL: {rss_url}")
        feed = feedparser.parse(rss_url)

        if feed.bozo:
            error_message = f"Error parsing RSS feed: {feed.bozo_exception}"
            logging.error(error_message)
            raise ValueError(error_message)

        titles = [entry.title for entry in feed.entries]

        logging.info(f"Successfully extracted {len(titles)} titles")
        return titles

    except Exception as e:
        logging.error(f"An error occurred while extracting headlines: {e}")
        return []

google_news_url = "https://news.google.com/news/rss"
headlines = get_headlines(google_news_url)

for headline in headlines:
    print(headline)
