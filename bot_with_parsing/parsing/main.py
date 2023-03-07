from .parsing_utils import get_last_page, get_soup
from .parse_info import get_all_products_from_page
from .db_utils import write_to_json


BASE_URL = 'https://www.kivano.kg'

def parse():
    category = '/igrushki'
    data = {}
    total_pages = get_last_page(get_soup(BASE_URL+category))
    for page in range(1, total_pages+1):
        url = BASE_URL + category + '?page=' + str(page)
        #'https://www.kivano.kg/igrushki?page=3'
        print(url)
        products = get_all_products_from_page(get_soup(url))
        data[page] = products
    write_to_json(data)
    
