import requests
from bs4 import BeautifulSoup
import os

if not os.path.isdir('textures'): os.mkdir('textures')
soup = BeautifulSoup(requests.get('https://texturehaven.com/textures/').content, 'lxml').find('div', {'id': 'item-grid'}).findAll('a')
for i in soup:
	url = 'https://texturehaven.com'+i['href']
	page_soup = BeautifulSoup(requests.get(url).content, 'lxml')
	title = page_soup.find('h1').find('b').text
	if not os.path.isdir('textures/'+title): os.mkdir('textures/'+title)
	print(title)
	inner_soup = page_soup.find('div', {'class': 'download-buttons'}).findAll('div', {'class': 'map-type'})
	for i in inner_soup:
		type_of_texture = i.find('div', {'class': 'map-download'}).find('p').text
		if not os.path.isdir(os.path.join('textures', title, type_of_texture)): os.mkdir(os.path.join('textures', title, type_of_texture))
		print(type_of_texture)
		for j in i.findAll('a'):
			resource = 'https://texturehaven.com'+j['href']
			print(resource)
			if not os.path.isfile(os.path.join('textures',title,type_of_texture,resource.split('/')[-1])):
				with open(os.path.join('textures',title,type_of_texture,resource.split('/')[-1]), 'wb') as writer:
					writer.write(requests.get(resource).content)
