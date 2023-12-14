import requests
import json
b = input("press 1 : ")
if (b == "1"):
    a = "technology"
    url = f"https://newsapi.org/v2/everything?q={a}&from=2023-10-06&sortBy=publishedAt&apiKey=92481e17476748bc8a55713783ebcb38"
    r = requests.get(url)
    news = json.loads(r.text)   
    for i in news["articles"]:
        print(i["title"])
        print(i["description"])
        print("------------------------")