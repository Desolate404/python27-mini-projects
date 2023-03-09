# import requests
# from bs4 import BeautifulSoup as BS

# "----Пагинация Машина кг----"
# BASE_URL = 'https://www.mashina.kg/search/all/'

# html = requests.get(BASE_URL).text
# soup = BS(html, 'lxml')
# pagination = soup.Find('ul', {'class':'pagination'})
# last_li = pagination.find_all('li')[-1]
# last_page = last_li.find('a').get('data-page')

'CSV'
import csv

data = [
    {'title':"hello", "price":342},
    {'title':"test", "price":7643},
    {'title':"aaa", "price":324},
    {'title':"bbb", "price":453},
]

with open("test,csv", "w") as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(data[0].keys())
    for product in data:
        writer.writerow(product.values())

