import requests
import random
import os

# call the disney api to get total results and then pick a random number and grab image
dapi_url='https://api.disneyapi.dev'
dapi_character_url = f'{dapi_url}/characters'
dapi_character_page_url = f'{dapi_character_url}?page='
image_folder = '/home/pi/dev/st7789-python/examples'

response = requests.get(dapi_character_url)
#print(response.json())

json = response.json()

#count = json['data']['count']
total_pages = json['totalPages']

# pick a random page between 1 and total pages

chosen_page = random.randrange(1, total_pages)

page_response = requests.get(f'{dapi_character_page_url}{chosen_page}')
page_json = response.json()

# pic element in returned page

count = page_json['count']
index = random.randrange(0, count)

item = page_json['data'][index]

print(item)

item_image = item['imageUrl']
item_name = item['name']

image_response = requests.get(item_image, stream=True)
with open(f'{image_folder}/dsny.image', 'wb') as f:
    for chunk in image_response:
        f.write(chunk)



os.system(f'{image_folder}/dsp-image.py {image_folder}/dsny.image')
