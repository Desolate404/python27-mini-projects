import requests
from bs4 import BeautifulSoup as BS
import csv

BASE_URL = 'https://www.mashina.kg'


def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

def description_info(product:BS):
    engine=product.find('p',{'class':'body-type'}).text.strip()
    specifications=product.find('p',{'class':'volume'}).text.strip()
    age = product.find('p',{'class':'year-miles'}).text.strip()
    city =product.find('p',{'class':'city'}).text.strip().split("\n")[0]
    return f'Двигатель: {engine} Спецификации: {specifications} Год {age} Город: {city}'

def get_product_info(product:BS) -> dict:
    title = product.find('h2').text.strip()
    let =product.find('p').text.strip().split('\n')
    price = let[0]+'/'+let[-1].lstrip()
    image = product.find('img').get('data-src')
    description = description_info(product)
    list_data=[title,price, description, image]
    write_to_csv(list_data)
    return list_data

def get_last_page(url)->int:
    soup = get_soup(url)
    pages = soup.find_all('li', {'class' : "page-item"})[-1].find('a').get('data-page')

    return int(pages)

def get_all_products_from_page(url:str) -> list:
    res = []
    soup = get_soup(url)
    box = soup.find('div',{'class':'table-view-list'})
    products = box.find_all('div',{'class':'list-item'})
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)
        
    return res

def write_to_csv(data):
    filename = 'car_data.csv'
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        for i in data:
            writer.writerow([i])
 
def main():
    category = '/motosearch/all/'
    data = []
    last_page = get_last_page(BASE_URL+category)
    for page in range(1,last_page+1):
        url = (BASE_URL+category+'?page='+str(page))
        print(url)
        one_page_data=get_all_products_from_page(url)
        data.append(one_page_data)

main()
