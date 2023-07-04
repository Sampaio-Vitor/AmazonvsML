import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Function to perform Amazon search
def getAmazonSearch(search_query):
    url = "https://www.amazon.com.br/s?k=" + search_query
    page = requests.get(url, headers=header)
    if page.status_code == 200:
        return page.content
    else:
        return "Error"

# Function to search product details by ASIN
def Searchasin(asin):
    url = "https://www.amazon.com.br/dp/" + asin
    page = requests.get(url, cookies=cookie, headers=header)
    if page.status_code == 200:
        return page.content
    else:
        return "Error"

# Function to search product reviews
def Searchreviews(review_link):
    url = "https://www.amazon.com.br" + review_link
    page = requests.get(url, cookies=cookie, headers=header)
    if page.status_code == 200:
        return page.content
    else:
        return "Error"
cookie={}
# Set up the base URL
base_url = "https://www.amazon.com.br/s?k="

# Read the product list from file
with open("missing_values.txt", "r") as file:
    products = file.read().splitlines()

# Set up the headers
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'referer': 'https://www.amazon.com/s?k=nike+shoes+men&crid=28WRS5SFLWWZ6&sprefix=nike%2Caps%2C357&ref=nb_sb_ss_organic-diversity_2_4'
}

# Create an empty DataFrame
df = pd.DataFrame(columns=['Search Query', 'Product Title', 'Link', 'Review'])

# Iterate through the product list with tqdm progress bar
for search_query in tqdm(products, desc="Processing Products"):
    # Create the search URL
    url = base_url + search_query

    # Send the search request
    search_response = getAmazonSearch(search_query)

    # Extract product names and ASINs
    product_names = []
    data_asin = []

    soup = BeautifulSoup(search_response, 'html.parser')

    for i in soup.findAll("span", {'class': 'a-size-base-plus a-color-base a-text-normal'}):
        product_names.append(i.text)

    for i in soup.findAll("div", {'class': "sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20"}):
        data_asin.append(i['data-asin'])

    # Scrape product details and reviews
    for asin in tqdm(data_asin, desc="Scraping Products"):
        response = Searchasin(asin)
        soup = BeautifulSoup(response, 'html.parser')

        product_title = soup.find("span", {'id': 'productTitle'})
        if product_title:
            title = product_title.text.strip()
        else:
            title = "N/A"

        for link in soup.findAll("a", {'data-hook': "see-all-reviews-link-foot"}):
            review_link = link['href']
            response = Searchreviews(review_link)
            soup = BeautifulSoup(response, 'html.parser')

            for review in soup.findAll("span", {'data-hook': "review-body"}):
                review_text = review.text.strip()

                # Add the data to the DataFrame
                df = df.append({
                    'Search Query': search_query,
                    'Product Title': title,
                    'Link': 'https://www.amazon.com.br/dp/' + asin,
                    'Review': review_text
                    
                }, ignore_index=True)
                df.to_csv("products_data.csv", index=False)

# Save the data as a single CSV file
df.to_csv("products_data2.csv", index=False)
