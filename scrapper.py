import requests

def fetchData(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)

url = "ENTER URL HERE"
fetchData(url, r"c:\Users\Pranav\Desktop\Python\data.html")
