import sys
import csv
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("\n[!] Error: Missing required libraries.")
    print("Please run the following command in your terminal:")
    print(f"{sys.executable} -m pip install requests beautifulsoup4")
    sys.exit(1)

def scrape_quotes(output_file="quotes.csv"):
    """
    Extracts quotes from 'http://quotes.toscrape.com' and saves them to a CSV.
    """
    url = "http://quotes.toscrape.com"
    print(f"--- Fetching data from {url} ---")
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        quote_elements = soup.find_all('div', class_='quote')
        
        scraped_data = []
        print(f"Found {len(quote_elements)} quotes. Processing...\n")
        
        for i, quote in enumerate(quote_elements, 1):
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            
            # Store data for CSV
            scraped_data.append({
                "ID": i,
                "Quote": text,
                "Author": author,
                "Tags": ", ".join(tags)
            })
            
            print(f"[{i}] Quote saved: '{text[:50]}...' by {author}")
        keys = scraped_data[0].keys()
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(scraped_data)
            
        print(f"\n--- Success! Data saved to {output_file} ---")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    scrape_quotes()
