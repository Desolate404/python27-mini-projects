"CRUD"
# create - создать
# read - читать
# update - обновлять
# delete - удалять

from products import create, read

while True:
    oper = input("c/r/u/d: ")
    if oper == 'c':
        create()
    elif oper == 'r':
        read()
