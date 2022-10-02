import nasapy
import json

import urllib.request
import os
import sys


search = input()
n = input()
sub_dir = os.popen('pwd').read().split('\n')[0]

print(sub_dir)

data = nasapy.media_search(query=search, media_type='image')

dir = search 
os.makedirs(dir)

file=dir+'.txt'


for value in data['items']:
    img = value['links'][0]['href']
    print(img)
    title = value['data'][0]['nasa_id']
    urllib.request.urlretrieve(img, os.path.join(dir,title+".jpg"))

astro_images = os.listdir(dir)

os.system('cd '+dir)
os.system('rclip -f -t '+n+' '+search+' > '+file)

with open(dir+'.txt', 'r') as f:
    pre_select = f.readlines()


select = [element.replace(sub_dir+'/'+search+'/', '').replace('.jpg\n', '') for element in pre_select]

print(select)

i = 0
new_data = data
items_data = []

for value in data['items']:
    if value['data'][0]['nasa_id'] not in select:
        items_data.append(value)
        i  = i + 1


#print(items_data)

new_data = {
    'collection' : {
        'version': '1.0',
        'href': 'http://api.insightinput.co/search?q=casablanca&media_type=image&page=1',
        'data' : items_data,
        'metadata': {
            'total_hits': i
        }
    }
}
print('_______________________')
print(new_data)
os.system('rm -rf '+file+' '+dir)
