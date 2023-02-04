import requests
from bs4 import BeautifulSoup

url = "https://www.zoominfo.com/#industry=322910"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
print(soup)