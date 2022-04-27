import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re
import requests
import lxml
from lxml.html.soupparser import fromstring
import prettify
import numbers
import htmltext

pd.set_option('max_colwidth', None)

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}
with requests.Session() as s:
    BASE_URL = 'https://www.zillow.com/homes/for_sale/'
    CITY = 'seattle/'
    NUMBER_OF_PAGES = 10

    url_list = []
    r_list = []
    soup_list = []
    address_list = []

    for page_num in range(NUMBER_OF_PAGES + 1):
        # Note: 0_p == 1_p == BASE_URL + CITY
        if page_num >= 1:
            url_var = BASE_URL + CITY + str(page_num) + '_p/'

            url_list.append(url_var)

            # add contents of urls to soup url_var from each url

            #r_var = 'r' + str(page_num)
            r_var = s.get(url_var, headers = req_headers)
            
            r_list.append(r_var)

            #s_var = 'soup' + str(page_num)
            s_var = BeautifulSoup(r_var.content, 'html.parser')
            
            soup_list.append(s_var)

            #df_var = 'df' + str(page_num)
            df_var = pd.DataFrame()
            

            address = s_var.find_all(class_= 'list-card-addr')
            price = list(s_var.find_all(class_='list-card-price'))
            beds = list(s_var.find_all("ul", class_="list-card-details"))
            # details = s_var.find_all ('div', {'class': 'list-card-details'})
            # home_type = s_var.find_all ('div', {'class': 'list-card-footer'})
            last_updated = s_var.find_all('div', {'class': 'list-card-variable-text list-card-img-overlay'})
            
            # brokerage = list(s_var.find_all(class_= 'list-card-brokerage list-card-img-overlay',text=True))
            # link = s_var.find_all (class_= 'list-card-link')

            # TODO: Create n-tuples of the various criteria . . .
            df_var['address'] = address
            df_var['prices'] = price
            df_var['beds'] = beds
            df_var['last_updated'] = last_updated

            #address_list.append(df_var['address'])
            #print(df_var['address'].to_string(index=False).replace("[","").replace("]",""))
            #print(df_var['prices'].to_string(index=False).replace("[","").replace("]",""))
            # print(df_var['beds'].to_string(index=False).replace("[","")
            #                                            .replace("]","")
            #                                            .replace(",  ,  , ","")
            #                                            .replace(" -","|")
            #                                            .replace("sqft,","")
            #                                            .replace(", ","|")
            #     )

            #print(df_var['last_updated'].to_string(index=False).replace("[","").replace("]","").replace("3D Homes Icon, , 3D Tour",""))
            break




#print(url_list)
#print(r_list)
#print(soup_list)
#print(address_list)

# soup = BeautifulSoup(r.content, 'html.parser')
# soup1 = BeautifulSoup(r2.content, 'html.parser')