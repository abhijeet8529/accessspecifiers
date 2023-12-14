from bs4 import BeautifulSoup
import requests
url = "https://www.google.co.in/?gfe_rd=cr&ei=szzrWMPlCuzs8Ae77Y6ABg"
d = requests.get(url)
# print(d.text)

soup = BeautifulSoup(d.text, 'html.parser')
print(soup.prettify())
for heading in soup.find_all('h2'):
    print(heading.text)
