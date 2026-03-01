import requests
response = requests.get("https://books.toscrape.com")
print(response)
print(response.status_code)
