import requests
from bs4 import BeautifulSoup
import os

url = "https://www.census.gov/naics/?48967"

# Make the request and parse the HTML
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links in the HTML
links = soup.find_all("a")

# Filter the links to only include those with the desired file extensions
files = [link["href"] for link in links if link["href"].endswith((".xlsx", ".pdf", ".xls"))]

# Download each file
for file in files:
    file_response = requests.get(file)
    file_name = os.path.basename(file)
    with open(file_name, "wb") as f:
        f.write(file_response.content)