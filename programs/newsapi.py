import requests
import json
print("1/for cricket news\n"
      "2/for technology news\n"
      "3/for social news\n"
      "4/for gaming news\n"
      "5/for political news\n"
      "search/for random\n"
      "0 to exit\n")
while True:
    query = input("Enter according to your choice or 0 to exit : ")
    if query == "search":
        a = input("search news for : ")    
    elif query == "1":
        a = "cricket"
    elif query == "2":
        a = "technology"
    elif query == '3':
        a = "social"
    elif query == "4":
        a = "gaming"
    elif query == "5":
        a = "politics"
    else:
        break
    
    url = f"https://newsapi.org/v2/everything?q={a}&from=2023-10-07&sortBy=publishedAt&apiKey=92481e17476748bc8a55713783ebcb38"
    r = requests.get(url)
    news = json.loads(r.text)   
    for i in news["articles"]:
        print(i["title"])
        print(i["description"])
        print("------------------------")
    
    
