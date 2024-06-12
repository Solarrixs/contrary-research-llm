import requests
from bs4 import BeautifulSoup
import time
import re

def get_google_search_results(query, start):
    headers = {
        'User-Agent': 'Mozilla/4.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/536.36'
    }
    params = {
        'q': query,
        'start': start,
        'num': 10
    }
    response = requests.get('https://www.google.com/search', headers=headers, params=params)
    response.raise_for_status()
    return response.text

def extract_urls_from_search_results(html):
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and 'https://research.contrary.com/reports/' in href:
            clean_url = re.sub(r'#.*$', '', href)  # Remove fragments
            if clean_url not in urls and not re.search(r'/search\?|%', clean_url):  # Exclude specific URLs
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

query = '"Breakdown" site:https://research.contrary.com/reports/'
all_urls = []
added_urls = []

try:
    # Read existing URLs
    existing_urls = read_existing_urls('List of Companies.txt')
    all_urls.extend(existing_urls)

    # Loop to extract new URLs
    for start in range(0, 100, 10): # Adjust range
        search_results_html = get_google_search_results(query, start)
        urls = extract_urls_from_search_results(search_results_html)
        new_urls = [url for url in urls if url not in all_urls]
        added_urls.extend(new_urls)
        all_urls.extend(new_urls)
        time.sleep(1)

    unique_urls = list(set(all_urls))
    write_urls_to_file('List of Companies.txt', unique_urls)

    print("URLs have been saved to List of Companies.txt")

    if added_urls:
        print("New URLs that were added:")
        for url in added_urls:
            print(url)

except Exception as e:
    print(f"An error occurred: {e}")