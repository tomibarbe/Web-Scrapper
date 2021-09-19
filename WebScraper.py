from bs4 import BeautifulSoup as soup
import time



from selenium import webdriver
url = "https://huitru.com"

DRIVER_PATH = r'C:\Users\Tomi\Desktop\WebScrape\chromedriver.exe'

#open the file, and read it:
f = open("main_page_html.txt", "a+") #TODO: Ver si se puede cambiar direccion del archivo. Ver lo de r+, w+, etc.
f.seek(0) #Dirige el cursor, que estaba al final del archivo para appendear, al inicio del archivo.
html = f.read()

print("espacio", html == '')
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

#if it does not have content, scrap and save it
if (html == ''):
    driver.get(url+'/11-caminos')

    html = driver.page_source

    f.write(html)
    print("html barbe")
    #print(html)
f.close()


page_soup = soup(html, 'html.parser')
#Agarra los caminos
caminos = page_soup.findAll("a", {"class":"productoItem column"})


#productos = 
# [
#  {
#    modelo: 'yamani',
#    precio: 123123,
#    foto_src: 'http://asdasd.com',
#    link: 'https://asdmadsa'
#  }
# ]

productos = []

for camino in caminos:
    #print(camino)
    modelo = camino.h2.text
    #print(modelo)
    link = camino.get('href')
    #producto.append({"modelo": modelo , "link": link, "variantes": []})
    #print(link)
    #Acá habria otra variable para que guarde el link de cada camino en cada iteración.
    #Luego esa variable se feedea al proximo scrap dentro de este loop.


#for producto in productos:
#TODO: Hacer lo de guardar en un archivo cada camino, y hacer lo de chequear si existe para no hacer todo de vuelta. Es lo de abajo for producto in productos:
link = productos[1]
driver.get(url+'/'+link)
html = driver.page_source
#print(html)
page_soup = soup(html, 'html.parser')

#for producto in productos:
#    titulo = producto.modelo
#    Si hago la request, no hace falta levantar la pagina con este scrapeo:
#    f = open(titulo + ".txt", "a+") #TODO: Ver si se puede cambiar direccion del archivo. Ver lo de r+, w+, etc.
#    f.seek(0) #Dirige el cursor, que estaba al final del archivo para appendear, al inicio del archivo.
#    html = f.read()
#    print("espacio", html == '') #Si es true, crea el archivo de nuevo. Si es false, lo lee del .txt.
#
#    #if it does not have content, scrap and save it
#    if (html == ''):
#        driver.get(url+'/11-caminos')
#
#        html = driver.page_source
#
#        f.write(html)
#        #print(html)
#    f.close()
#    page_soup = soup(html, 'html.parser')
#    #Acá va el scrape de cada producto
#    detalle_producto = page_soup.findAll("div", class_="productoPage row")
#    #Para hacer la request necesito el id de cada camino. El id lo obtengo de producto.link. Lo tengo que splitear 2 veces para obtener solo el id. 
#    #Esto obtiene el id que necesitás para la request:
#    (producto.link.split('/'))[1].split('-')[0]
#    #Request de python para que me traiga la info de las variantes. Cuidado: Devuelve un json. Tendría que ver cómo obtener el json y cómo interactuar.
#    #Loopea cada variante dentro de la request:
#        #Suma variante al producto.variantes, que corresponde a un array.


producto = page_soup.findAll("div", class_="productoPage row")
#producto = page_soup.findAll("div")
#print(producto)
#titulo = producto.h1
#print(titulo)

   
    
for unidad in producto:
    nombre = unidad.h1.text
    descripcion = page_soup.find("div", class_="productoPage-collapsable")
    #descripcion = page_soup.get_text("div", class_="productoPage-collapsable")

    
    #color = page_soup.find("div", class_="productoPage-thumb style01 column")
    #print(nombre + ' ' + color)
    #print(color)
    print (descripcion.text)


color_container = page_soup.find("div", class_="productoPage-thumb-container small-up-4 medium-up-6 cf")
variantes = color_container.findAll('a')
for variante in variantes:
    print(variante.get('title'))
    
