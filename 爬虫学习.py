import requests
response = requests.get("https://books.toscrape.com")
if response.ok:
    print("请求成功")
else:
    print("请求失败")