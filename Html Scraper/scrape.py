from bs4 import BeautifulSoup
import requests

url = input()
response = requests.get(url, timeout = 6)
content = BeautifulSoup(response.content, "html.parser")

print(content)

