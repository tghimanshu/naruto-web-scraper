import requests
from bs4 import BeautifulSoup
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LinkExtractor:
    """
    A tool for extracting detailed information from character pages.

    This class reads a JSON file containing character links, visits each link,
    and fetches the page content.
    """

    BASE_URL = "https://naruto.fandom.com"

    def __init__(self, input_file):
        """
        Initializes the LinkExtractor.

        Args:
            input_file (str): The path to the input JSON file containing character data.
        """
        self.input_file = input_file
        self.characters = self.load_characters()

    def load_characters(self):
        """
        Loads character data from the input JSON file.

        Returns:
            list: A list of dictionaries representing characters, or an empty list if loading fails.
        """
        try:
            with open(self.input_file, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading characters from {self.input_file}: {e}")
            return []

    def fetch_character_page(self, relative_link):
        """
        Fetches the content of a character's wiki page.

        Args:
            relative_link (str): The relative URL path to the character's page (e.g., '/wiki/Naruto_Uzumaki').

        Returns:
            BeautifulSoup: A BeautifulSoup object of the parsed HTML, or None if an error occurs.
        """
        url = f"{self.BASE_URL}{relative_link}"
        try:
            logging.info(f"Fetching {url}")
            response = requests.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            logging.error(f"Error fetching URL {url}: {e}")
            return None

    def process_characters(self, limit=None):
        """
        Iterates through the loaded characters and fetches their pages.

        Args:
            limit (int, optional): The maximum number of characters to process. Defaults to None (process all).
        """
        count = 0
        for member in self.characters:
            if limit is not None and count >= limit:
                break

            if 'link' in member:
                soup = self.fetch_character_page(member['link'])
                if soup:
                    # In a real scenario, you would parse 'soup' here to extract specific details.
                    # For this demonstration, we just log success.
                    logging.info(f"Successfully parsed page for {member.get('name', 'Unknown')}")
                    # Example: print(soup.title.string)

            count += 1

if __name__ == "__main__":
    # Example usage:
    # Ensure 'characters.json' exists before running this.
    extractor = LinkExtractor('characters.json')

    # Just processing the first item as a demo to avoid spamming the server
    extractor.process_characters(limit=1)
