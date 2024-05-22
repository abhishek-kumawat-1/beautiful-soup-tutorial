import requests


def fetchSaveToFile(url,path):
    r=requests.get(url)
    with open(path,"wb") as f:
        f.write(r.content)

url="https://timesofindia.indiatimes.com/city/delhi"

# r=requests.get(url)
# print(r.text)

fetchSaveToFile(url,"data/times.html")