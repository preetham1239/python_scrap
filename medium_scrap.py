import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://onezero.medium.com/the-star-wars-disney-theme-park-is-a-little-too-authentic-6b8e9a3efe1a")
soup = BeautifulSoup(response.text, "html.parser")
title1 = soup.find("title").get_text()
a=soup.find_all("p")
print(title1)
for i in a:
	print(i.get_text())

