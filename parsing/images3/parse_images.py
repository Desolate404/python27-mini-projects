import requests, json

image_url = 'https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg'

response = requests.get(image_url)

with open("test.jpg", "wb") as file:
    file.write(response.content)