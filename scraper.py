import requests
from bs4 import BeautifulSoup
resp = requests.get("http://www.ivytofraudulentgame.com/live/").text
try:
    soup = BeautifulSoup(resp, "lxml")
except:
    soup = BeautifulSoup(resp, "html5lib")
print(soup.find("body"))
