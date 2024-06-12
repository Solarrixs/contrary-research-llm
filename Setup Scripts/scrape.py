import requests
from bs4 import BeautifulSoup
import json
import re
import os

os.makedirs('Output', exist_ok=True)

with open("List of Companies.txt", 'r') as file:
    urls = file.readlines()

urls = [url.strip() for url in urls]

for url in urls:
    try:
        response = requests.get(url)
        response.raise_for_status()
        webpage_content = response.text

        soup = BeautifulSoup(webpage_content, 'html.parser')

        script_tag = soup.find('script', type='application/json')
        if not script_tag:
            raise ValueError("No script tag with type 'application/json' found")

        json_data = script_tag.string
        if not json_data:
            raise ValueError("No JSON data found in the script tag")

        data = json.loads(json_data)
        title = data['props']['pageProps']['page']['data']['title'][0]['text']

        page_data = data['props']['pageProps']['page']['data']['slices']
        extracted_text = []
        for slice in page_data:
            if 'primary' in slice and 'text' in slice['primary']:
                for item in slice['primary']['text']:
                    if item['type'] == 'paragraph':
                        extracted_text.append(item['text'])
        full_text = '\n'.join(extracted_text)

        valid_filename = re.sub(r'[\\/*?:"<>|]', "", title) + ".txt"

        with open(f"Output/{valid_filename}", 'w', encoding='utf-8') as file:
            file.write(f"{title}\n\n{full_text}")
    
    except Exception as e:
        print(f"Failed to process URL: {url}")
        print(f"Error: {e}")