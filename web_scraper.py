import requests
from bs4 import BeautifulSoup as bs
import tkinter as tk
from tkinter import filedialog

# Ask user to select the download destination
root = tk.Tk()
root.withdraw()
folder_path = filedialog.askdirectory()

url = input("Enter the URL of the website you want to scrape: ")
response = requests.get(url)

soup = bs(response.text, 'html.parser')

# Download all content with the extensions mp4, webm, or png
for link in soup.find_all('a', href=True):
    href = link['href']
    if href.endswith(('mp4', 'webm', 'png')):
        filename = href.split('/')[-1]
        content = requests.get(href).content
        with open(f"{folder_path}/{filename}", 'wb') as f:
            f.write(content)
            print(f"Downloaded {filename}")
