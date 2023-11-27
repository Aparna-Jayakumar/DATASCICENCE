import requests
from bs4 import BeautifulSoup
def getdata(url):
    r = requests.get(url)
    return  r.content
htmldata = getdata("https://www.w3schools.com/python/")
soup = BeautifulSoup(htmldata, 'html.parser')
data = ''
pr = len(soup.find_all('p'))
print("p tag:",pr)
for data in soup.find_all('p'):
    print(data.getText())