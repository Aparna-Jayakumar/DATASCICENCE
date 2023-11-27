import requests
from bs4 import BeautifulSoup
def getdata(url):
    r = requests.get(url)
    return r.content
htmldata = getdata("https://www.w3schools.blog/python-tutorial")
soup = BeautifulSoup(htmldata,'html.parser')
links = soup.find_all("a")
print("links:",len(links))
for link in links:
    if link.get("href") != "":
        print("Link:", link.getText("herf"), "Text :",link.string)