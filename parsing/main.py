import json
import requests
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://www.kivano.kg'

def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

def get_product_info(products: BS) -> dict:
    title = products.find('div', {'class':'listbox_title'}).text.strip()
    price = products.find('div', {'class':'listbox_price'}).text.strip().split('\n')[0]
    image = products.find('div', {'class':'listbox_img'}).find('img').get('src')
    return{'title':title, 'price':price, 'image':BASE_URL+image}


def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('div', {'class':'list-view'})
    products = box.find_all('div',{'class':'product_listbox'})
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)
    #print(res)
    return res

def write_in_json(data:list):
    with open('db.json','w', encoding='utf-8') as file:
        json.dump(data , file, ensure_ascii=False)

def get_last_page(url:str) -> int:
    soup = get_soup(url)
    last = soup.find('li',{'class','last'})
    return int(last.text)

def main():
    category = '/noutbuki'
    data = {}
    last_page = get_last_page(BASE_URL + category)
    for page in range(1, last_page+1):
        url = BASE_URL + category + '?page=' + str(page)
        print(url)
        one_page_data = get_all_products_from_page(url)
        data[page] = one_page_data
    write_in_json(data)


main()