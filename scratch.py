import requests
from bs4 import BeautifulSoup

response = requests.get(YOUTUBE_URL)

print("Status code", response.status_code)

with open('trending.html', 'w') as f:
  f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')
print('Page Title: ', doc.title)