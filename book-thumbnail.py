#!/usr/bin/python

'''
Author: Max Russell, max@theguards.net
tool to work with openlibary api 
'''
import requests
import json
from PIL import Image
import re


r = requests.get('https://openlibrary.org/api/books?bibkeys=ISBN:9781492051367&format=json')

y = r.json()

x = y['ISBN:9781492051367']

print(x)

thumbnail_small = x['thumbnail_url']

source = thumbnail_small
thumbnail_large = re.sub('-S', '-L', source)

print(thumbnail_large)

#url = x['thumbnail_url']
url = thumbnail_large
req = requests.get(url)

with open('./thumbnail.jpg', 'wb') as f:
	f.write(req.content)
print('done')

img = Image.open('./thumbnail.jpg')
# newsize = (500, 500)
# img1 = img.resize(newsize)
#img1.show()
img.show()
