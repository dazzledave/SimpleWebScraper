import requests
from bs4 import BeautifulSoup
import csv

# This script only saves haedline tags for now.
def fetch_page(url):
    """Fetch content from the URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None

def extract_headlines(html):
    """Extract headlines from the HTML content."""
    soup = BeautifulSoup(html, 'html.parser')
    headlines = []
    
    # Example: Scraping h2 headlines (adjust for the website you're targeting)
    for headline in soup.find_all('h2'):
        headlines.append(headline.get_text(strip=True))
    
    return headlines

def save_to_csv(data, filename):
    """Save the extracted headlines to a CSV file."""
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Headline'])  # Writing the header
        for item in data:
            writer.writerow([item])  # Writing each headline

def main():
    url = input("Enter the URL of the website to scrape: ")
    html = fetch_page(url)
    
    if html:
        headlines = extract_headlines(html)
        
        if headlines:
            print(f"Found {len(headlines)} headlines.")
            save_to_csv(headlines, 'headlines.csv')
            print("Headlines saved to 'headlines.csv'.")
        else:
            print("No headlines found.")
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    main()
