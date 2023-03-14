import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website
url = "https://www.linkedin.com/jobs/search/?keywords=dev%20front-end%20d%C3%A9veloppeur%20web&location=France"
headers = {'User-Agent': 'Mozilla/5.0'}
params = {'sortBy': 'postedDate'}
response = requests.get(url, headers=headers, params=params)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the job listings
job_listings = soup.find_all("li", class_="result-card")

# Print the sorted job listings
for job_listing in job_listings:
    print job listing information
