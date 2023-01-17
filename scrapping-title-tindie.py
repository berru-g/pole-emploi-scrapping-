
"""
SRC / OPENAI
Il est important de pratiquer cela dans des environnements de test pour éviter de bloquer votre ip.
from fake_useragent import UserAgent

ua = UserAgent()

headers = {
    'User-Agent': ua.random,
}

response = requests.get(url, headers=headers)

"""

import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website
url = "https://www.tindie.com/browse/"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements with class "product-title"
titles = soup.find_all(class_="product-title")

# Print the titles
for title in titles:
    print(title.text)
