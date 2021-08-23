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

#chrome_options = Options()  
#chrome_options.add_argument("--headless") # Opens the browser up in background

#with Chrome(options=chrome_options) as browser:
#     browser.get(url+'/11-caminos')


page_soup = soup(html, 'html.parser')
caminos = page_soup.findAll("a", {"class":"productoItem column"})

#myurl = 'https://huitru.com'

#Opening connection and grabbing the page

#uClient = uReq(myurl+'/11-caminos')
#page_html = uClient.read()
#uClient.close()

#HTML Parsing
#page_soup = soup(page_html, "html.parser")


#Agarra los caminos
#caminos = page_soup.findAll("a", {"class":"productoItem column"})
product_links = []

for camino in caminos:
    #print(camino)
    modelo = camino.h2.text
    #print(modelo)
    precio = camino.span.text
    #print(precio)
    fotos_src = camino.img
    #print(fotos_src['src'])
    links = camino.get('href')
    product_links.append(links)
    #print(link)
    #Acá habria otra variable para que guarde el link de cada camino en cada iteración.
    #Luego esa variable se feedea al proximo scrap dentro de este loop.

#for link in product_links:
link = product_links[1]
driver.get(url+'/'+link)
html = driver.page_source
#print(html)
page_soup = soup(html, 'html.parser')

#page_html = uClient.read()
#time.sleep(20)
#uClient.close()
#HTML Parsing
#page_soup = soup(page_html, "html.parser")

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
    



