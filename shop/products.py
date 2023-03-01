from utils import get_products, update_products

def create():
    title = input("Введите название: ")
    price = float(input("Введите цену: "))
    #принимаем данные

    new_product = {"title":title, "price":price}
    #собираем в словарь

    products = get_products()
    #получаем список старых продуктов
    products.append(new_product)
    #добавляем в список новые данные
    update_products(products)
    #перезаписываем файл с новыми данными

def read():
    products = get_products()
    #получаем список продуктов
    for product in products:
        #проходим по каждому продукту и принтим
        print(f"""
===========================
название: {product['title']}
Цена: {product['price']}
===========================   
""")


def delete():
    products = get_products()
    print("Выведите продукт для удаления: ")
    for ind, prod in enumerate(products):
        print(f"{ind} => {prod['title']}")
    index = input()
    products.pop(index)
    update_products(products)

def update():
    products = get_products()
    print("Выведите продукт для обновления: ")
    for ind, prod in enumerate(products):
        print(f"{ind} => {prod['title']}")
    index = int(input())
    prod = products[index]
    print(f"""
    название: {prod['title']}
    Цена:     {prod['price']})
""")
    field = (input("Какое поле хотите обновить?,(title, price)\n"))
    value = input("Введите значение для этого поля: ")
    if field == 'title':
        prod['title'] = value
    elif field == 'price':
        prod['price'] = float(value)
    update_products(products)