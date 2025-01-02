import requests
from bs4 import BeautifulSoup

def web_scraper(url):
    # 1. Fetch the page HTML
    response = requests.get(url)
    
    # 2. Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 3. Extract specific elements — in this case, all <h1> tags
    headings = soup.find_all('h1')
    
    # 4. Print out each heading
    print(f"Headings found on {url}:")
    for h in headings:
        print("-", h.get_text(strip=True))

# Example usage:
if __name__ == "__main__":
    test_url = "https://example.com/"
    web_scraper(test_url)
