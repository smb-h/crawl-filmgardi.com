import requests
from bs4 import BeautifulSoup
import json


# url = "https://filmgardi.com/s/new"
url = "https://ghatreh.filmgardi.com/_api/_v10/Contents/Structure/Row/NormalAuto/24030?page=1&limit=50"
response = requests.get(url)
# print(response.status_code)
# print(response.content)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

def get_page(pg_num):
    url = "https://ghatreh.filmgardi.com/_api/_v10/Contents/Structure/Row/NormalAuto/24030?limit=200page="
    if pg_num > 1:
        url = url + str(pg_num)
    response = requests.get(url)
    json_data = json.loads(response.text)
    return json_data.get("body").get("result")


# Main loop
data = []
# for page_num in range(1, pages+1):
for page_num in range(1, 100):
    page = get_page(page_num)
    for movie in page:
    	data.append({
    		"title": movie.get("title"),
    		"poster": "https://ghatreh.filmgardi.com" + movie.get("poster")[0].get("url"),
    		"link": "https://filmgardi.com/p" + movie.get("alias"),
    		})


with open('data.txt', 'w', encoding='utf8') as outfile:
    json.dump(data, outfile, ensure_ascii=False)






