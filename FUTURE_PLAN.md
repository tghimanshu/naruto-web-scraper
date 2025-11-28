# Future Plan

This document outlines the roadmap for the Naruto Fandom Scraper project. Phase 1 is considered complete with the current refactoring and documentation. Phase 2 focuses on enhancements and feature expansions.

## Phase 1: Foundation (Complete)

-   **Refactoring**: The original Jupyter Notebooks have been refactored into modular Python scripts (`src/naruto_scraper.py` and `src/link_extractor.py`).
-   **Documentation**: Codebase fully documented with docstrings for all classes and methods. `README.md` updated with setup and usage instructions.
-   **Reliability**: Added logging and error handling to network requests and file operations.

## Phase 2: Enhancements (Future)

### 1. Data Extraction Improvements
-   **Detailed Parsing**: Enhance `LinkExtractor` to parse detailed information from character pages (e.g., Jutsu list, Rank, Affiliation, Family).
-   **Data Normalization**: Implement data cleaning to handle inconsistent formatting on the wiki pages.
-   **Output Formats**: Support exporting data to CSV or a database (SQLite/PostgreSQL) in addition to JSON.

### 2. Performance Optimization
-   **Asyncio**: Implement asynchronous requests using `aiohttp` to significantly speed up the scraping process.
-   **Rate Limiting**: Add polite crawling features to respect the wiki's `robots.txt` and avoid getting blocked.

### 3. Usability and CLI
-   **Command Line Arguments**: Use `argparse` to allow users to specify output files, limits, and other options via command line flags.
-   **Configuration File**: Support a `config.yaml` or `.env` file for managing URLs and settings.

### 4. Testing and Quality Assurance
-   **Unit Tests**: Write unit tests for parsing logic using `pytest`.
-   **Integration Tests**: Create tests that verify the full pipeline from scraping to saving.
-   **CI/CD**: Set up GitHub Actions to run tests and linters on every commit.

### 5. Frontend Visualization
-   **Dashboard**: Develop a simple web interface (using Flask or Streamlit) to browse and filter the scraped character data.
-   **Image Gallery**: Create a gallery view of all character thumbnails.

## Phase 3: Advanced Features

-   **Search Indexing**: Integrate with a search engine like Elasticsearch to allow full-text search over character bios.
-   **Relationship Mapping**: Analyze internal links to build a graph of character relationships.
-   **Automatic Updates**: Set up a scheduled job (cron) to periodically re-scrape and update the dataset.
