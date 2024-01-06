from bs4 import BeautifulSoup
import requests
url = "https://www.google.co.in/?gfe_rd=cr&ei=szzrWMPlCuzs8Ae77Y6ABg"
d = requests.get(url)
# print(d.text)

soup = BeautifulSoup(d.text, 'html.parser')
# print(soup.contents)
a = soup.select('div')
# print(a[2].getText())
# print(str(a[2]))
# for heading in soup.find_all('h2'):
#     print(heading.text)
print(a[1].get('id'))