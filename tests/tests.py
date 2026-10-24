from bs4 import BeautifulSoup 
import requests

url = "https://g1.globo.com/"
response = requests.get(url, timeout=10)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
h2_element = soup.find_all("h2")

print(h2_element)