from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome()
browser.get(start_url)

scraped_data=[]

def scrap ():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    tabla = soup.find("table", attrs={"class","wikitable sortable jquery-tablesorter"})
    body = tabla.find("tbody")
    celdas = body.find_all("tr")
    
    for celda in celdas:
        table_colts = celda.find_all("td")
        temp_list=[]
        for datos in table_colts:
            dato = datos.text.strip()
            print(dato)
            temp_list.append(dato)
        scraped_data.append(temp_list)
scrap()

stars_data=[]
for star in range(0,len(scraped_data)):
    star_name = scraped_data[star][1]
    distance = scraped_data[star][3]
    mass = scraped_data[star][5]
    radius = scraped_data[star][6]
    lum = scraped_data[star][7]

    required_data =[star_name, distance, mass, radius, lum]
    stars_data.append(required_data)

headers=["Star_Name","Distance","Mass","Radius","Luminosity"]
estrella = pd.DataFrame(stars_data, columns=headers)
estrella.to_csv("mi_resultado.csv",index=True, index_label="id")
