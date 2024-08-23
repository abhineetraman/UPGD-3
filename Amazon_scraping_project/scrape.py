import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def get_amazon_product_links(category_url, max_items=100):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://www.google.com/",
        "DNT": "1",  # Do Not Track Request Header
    }
    
    product_links = []
    page = 1
    
    while len(product_links) < max_items:
        url = f"{category_url}&page={page}"
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to retrieve page {page} for URL: {url} (Status Code: {response.status_code})")
            break
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if '/dp/' in href and href not in product_links:
                product_links.append("https://www.amazon.com" + href)
                if len(product_links) >= max_items:
                    break
        
        page += 1
        time.sleep(2)
    
    return product_links

def scrape_amazon_categories(categories):
    all_data = []

    for category_name, category_url in categories.items():
        print(f"Scraping category: {category_name}")
        product_links = get_amazon_product_links(category_url)
        if product_links:  # Only append if links are found
            category_data = {
                "Category": category_name,
                "Product_Link": product_links
            }
            df_category = pd.DataFrame(category_data)
            all_data.append(df_category)
        else:
            print(f"No links retrieved for category: {category_name}")

    df_all_categories = pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()
    return df_all_categories

categories = {
    "Footwear": "https://www.amazon.com/s?k=footwear",
    "Music Accessories": "https://www.amazon.com/s?k=music+accessories",
    "Bedding": "https://www.amazon.com/s?k=bedding",
    "Office Supplies": "https://www.amazon.com/s?k=office+supplies",
    "Camping Gear": "https://www.amazon.com/s?k=camping+gear",
    "Haircare": "https://www.amazon.com/s?k=haircare",
    "Car Accessories": "https://www.amazon.com/s?k=car+accessories",
    "Sports & Fitness": "https://www.amazon.com/s?k=sports+fitness"
}

df_all_categories = scrape_amazon_categories(categories)

if not df_all_categories.empty:
    df_all_categories.to_csv("Amazon_scraping_project/amazon_product_links.csv", index=False)
    print("Scraping complete. Data saved to amazon_product_links.csv")
else:
    print("No data scraped, CSV file not created.")
