import requests
import re
import random
from dotenv import load_dotenv
import os

def get_google_search_results(api_key, cse_id, query, start):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
        'start': start,
        'num': 10
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def extract_urls_from_search_results(json_data):
    urls = []
    for item in json_data.get('items', []):
        href = item.get('link')
        if href and 'https://research.contrary.com/reports/' in href:
            clean_url = re.sub(r'#.*$', '', href)
            if clean_url not in urls and not re.search(r'/search\?|%', clean_url):
                urls.append(clean_url)
    return urls

def read_existing_urls(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            existing_urls = file.read().splitlines()
    except FileNotFoundError:
        existing_urls = []
    return existing_urls

def write_urls_to_file(filename, urls):
    with open(filename, 'w', encoding='utf-8') as file:
        for url in urls:
            file.write(f"{url}\n")

query = '"Business Breakdown"'
all_urls = []
added_urls = []

def search_urls(api_key, cse_id):
    try:
        existing_urls = read_existing_urls('List of Companies.txt')
        all_urls.extend(existing_urls)

        page_indices = list(range(1, 999, 10))
        random.shuffle(page_indices)

        for start in page_indices:
            search_results_json = get_google_search_results(api_key, cse_id, query, start)
            urls = extract_urls_from_search_results(search_results_json)
            new_urls = [url for url in urls if url not in all_urls]
            added_urls.extend(new_urls)
            all_urls.extend(new_urls)

        unique_urls = list(set(all_urls))
        write_urls_to_file('List of Companies.txt', unique_urls)

        print("URLs have been saved to List of Companies.txt")

        if added_urls:
            print("New URLs that were added:")
            for url in added_urls:
                print(url)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    load_dotenv()
    API_KEY = os.getenv("GOOG_API_KEY")
    CSE_ID = os.getenv("CSE_ID")
    try:
        search_urls(API_KEY, CSE_ID)
        
    except Exception as e:
        print(f"An error occurred: {e}")