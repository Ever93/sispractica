from bs4 import BeautifulSoup
import requests
datos = requests.urlopen(‘https://www.openwebinars.net’).read().decode()


soup =  BeautifulSoup(datos)
tags = soup(‘a’)
for tag in tags:
		print(tag.get(‘href’))