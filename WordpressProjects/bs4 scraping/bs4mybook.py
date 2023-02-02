from bs4 import BeautifulSoup
import requests

# Define the URL to scrape
url = "https://www.royalroad.com/fiction/30172/idle-dreamer-first-world"

# Make a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the chapter links
chapter_links = soup.find_all("a", class_="chapter-link")

# Create an empty list to store the chapter data
chapters = []

# Loop through the chapter links
for link in chapter_links:
    # Get the chapter URL
    chapter_url = link["href"]
    # Make a request to the chapter URL
    chapter_response = requests.get(chapter_url)
    # Parse the HTML content
    chapter_soup = BeautifulSoup(chapter_response.content, "html.parser")
    # Get the chapter title
    chapter_title = chapter_soup.find("h1", class_="chapter-title").text
    # Get the chapter text
    chapter_text = chapter_soup.find("div", class_="chapter-text").text
    # Get the chapter date
    chapter_date = chapter_soup.find("div", class_="chapter-date").text
    # Append the chapter data to the list
    chapters.append({
        "title": chapter_title,
        "text": chapter_text,
        "date": chapter_date
    })

# Write the chapter data to a document
with open("book_chapters.txt", "w") as file:
    for chapter in chapters:
        file.write(chapter["title"] + "\n")
        file.write(chapter["text"] + "\n")
        file.write(chapter["date"] + "\n")