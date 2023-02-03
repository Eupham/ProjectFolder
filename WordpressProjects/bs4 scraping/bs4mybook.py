import requests
from bs4 import BeautifulSoup

# Request the website content
root_url = "https://www.royalroad.com"
book_url = "https://www.royalroad.com/fiction/30172/idle-dreamer-first-world"
req = requests.get(book_url)
soup = BeautifulSoup(req.text, "html.parser")

# Find the links to chapters
chapter_links = soup.find_all("a", href=True)
chapter_urls = [link["href"] for link in chapter_links if "/fiction/30172/idle-dreamer-first-world/chapter" in link["href"]]

# Request each chapter and save to a text file
for i, chapter_url in enumerate(chapter_urls):
    chapter_req = requests.get(root_url + chapter_url)
    with open(f"chapter_{i + 1}.txt", "w") as f:
        f.write(chapter_req.text)