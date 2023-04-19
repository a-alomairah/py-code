import requests
from bs4 import BeautifulSoup as bs

url = input("provide the url: ")
response = requests.get(url)

soup = bs(response.text, 'html.parser')

# Find all links on the page
for link in soup.find_all('a'):
    print(link.get('href'))

# Find all headings on the page
for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    print(heading.text.strip())
