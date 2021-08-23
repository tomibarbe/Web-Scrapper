from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time

myurl = 'https://huitru.com'

#Opening connection and grabbing the page

uClient = uReq(myurl+'/11-caminos')
page_html = uClient.read()
uClient.close()

#HTML Parsing
page_soup = soup(page_html, "html.parser")


#Agarra los caminos
caminos = page_soup.findAll("a", {"class":"productoItem column"})
product_links = []

for camino in caminos:
    #print(camino)
    modelo = camino.h2.text
    print(modelo)
    precio = camino.span.text
    print(precio)
    fotos_src = camino.img
    print(fotos_src['src'])
    links = camino.get('href')
    product_links.append(links)
    #print(link)
    #Acá habria otra variable para que guarde el link de cada camino en cada iteración.
    #Luego esa variable se feedea al proximo scrap dentro de este loop.

#for link in product_links:
link = product_links[1]
uClient = uReq(myurl+'/'+link)

page_html = uClient.read()
time.sleep(20)
uClient.close()
#HTML Parsing
page_soup = soup(page_html, "html.parser")

producto = page_soup.find("div", {"class":"productoPage row"})
print(producto)
titulo = producto.h1.text
print(titulo)

    