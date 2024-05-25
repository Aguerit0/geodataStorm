import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import re
import openpyxl
import plotly.express as px


class GetData:
    def __init__(self, base_url='https://wdc.kugi.kyoto-u.ac.jp/dst_final/'):
        self.base_url = base_url

    def get_data_by_month(self, year, month):
        if(int(month)>9):
            url = f'{self.base_url}{year}{month}/index.html'
        else:
            url = f'{self.base_url}{year}0{month}/index.html'
        return url
    
    def get_data_by_year(self, year):
        url = f'{self.base_url}{year}/index.html'
        return url
    
    def scrapping_data(self, url):
        page = requests.get(url)
                
        soup = BeautifulSoup(page.content, 'html.parser')

        # Obtención de datos del texto
        data_text = soup.get_text()

        # Encontrar números enteros en el texto
        data_values = [int(value) for value in re.findall(r'-?\d+', data_text)]

        # Dividimos los datos en sublistas para cada día
        day_length = 24
        all_day_data = [data_values[i:i+day_length] for i in range(26, len(data_values), day_length+1)]
        dataframe = pd.DataFrame(all_day_data)
        return dataframe