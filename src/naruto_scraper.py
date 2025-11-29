import requests
from bs4 import BeautifulSoup
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NarutoScraper:
    """
    A scraper for fetching character information from the Naruto Fandom Wiki.

    This class handles fetching pages, parsing character data (names, links, images),
    and saving the data to a JSON file.
    """

    BASE_URL = "https://naruto.fandom.com"
    CATEGORY_URLS = [
        "https://naruto.fandom.com/wiki/Category:Characters",
        "https://naruto.fandom.com/wiki/Category:Characters?from=Fugai%0AFugai",
        "https://naruto.fandom.com/wiki/Category:Characters?from=H%C5%8Dki+%28Watari%29%0AH%C5%8Dki+%28Watari%29",
        "https://naruto.fandom.com/wiki/Category:Characters?from=Kohari+Umino%0AKohari+Umino",
        "https://naruto.fandom.com/wiki/Category:Characters?from=Nang%C5%8D%0ANang%C5%8D",
        "https://naruto.fandom.com/wiki/Category:Characters?from=Shishio%0AShishio",
        "https://naruto.fandom.com/wiki/Category:Characters?from=Uroko+Kurama%0AUroko+Kurama"
    ]

    def __init__(self):
        """
        Initializes the NarutoScraper.
        """
        self.character_data = []

    def fetch_page(self, url):
        """
        Fetches the content of a given URL.

        Args:
            url (str): The URL to fetch.

        Returns:
            BeautifulSoup: A BeautifulSoup object of the parsed HTML, or None if an error occurs.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            logging.info(f"Successfully fetched {url}")
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            logging.error(f"Error fetching URL {url}: {e}")
            return None

    def scrape_characters(self):
        """
        Iterates through the category URLs, fetches pages, and extracts character information.

        This method populates the self.character_data list with dictionaries containing:
        - id: A unique integer ID.
        - link: The relative URL to the character's wiki page.
        - name: The character's name.
        - imageUrl: The URL of the character's thumbnail image.
        """
        character_id = 0
        for url in self.CATEGORY_URLS:
            soup = self.fetch_page(url)
            if not soup:
                continue

            atags = soup.select('.category-page__member-link')
            imgtags = soup.select('.category-page__member-thumbnail')

            for link_tag in atags:
                character_name = link_tag.getText()
                character_link = link_tag.get('href')

                # Find associated image
                image_url = None
                for img_tag in imgtags:
                    if img_tag.get('alt') == character_name:
                        image_src = img_tag.get('data-src') or img_tag.get('src')
                        if image_src:
                            # Clean up the image URL (remove revision parameters)
                            split_img = image_src.split('/revision')
                            image_url = split_img[0]
                        break

                if image_url:
                    self.character_data.append({
                        'id': character_id,
                        'link': character_link,
                        'name': character_name,
                        'imageUrl': image_url
                    })
                    character_id += 1

        logging.info(f"Scraped {len(self.character_data)} characters.")

    def save_to_json(self, filepath):
        """
        Saves the scraped character data to a JSON file.

        Args:
            filepath (str): The path to the output JSON file.
        """
        try:
            with open(filepath, 'w') as f:
                json.dump(self.character_data, f, indent=4)
            logging.info(f"Successfully saved data to {filepath}")
        except IOError as e:
            logging.error(f"Error saving data to {filepath}: {e}")

    def run(self, output_file='characters.json'):
        """
        Executes the scraping process and saves the result.

        Args:
            output_file (str): The filename for the JSON output. Defaults to 'characters.json'.
        """
        self.scrape_characters()
        self.save_to_json(output_file)

if __name__ == "__main__":
    scraper = NarutoScraper()
    scraper.run()
