import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
response = requests.get("https://movie.douban.com/top250",headers=headers)
print(response.text)
