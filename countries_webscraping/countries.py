from bs4 import BeautifulSoup, Tag, NavigableString
import requests
import pandas as pd

COUNTRIES_URL = 'https://www.worldometers.info/geography/alphabetical-list-of-countries/'
GDP_URL = 'https://www.worldometers.info/gdp/gdp-per-capita/'

def country_total(soup: BeautifulSoup) -> list:
     '''
     This function scrapes all the country names with Beautiful Soup and returns
     a list

     Argument: Beautiful soup
     Return: a list of strings (country names)

     '''
     countries = soup.find_all('tr')
     counter = 0
     total_countries = []
     for country in countries:
          if counter == 0: # don't add the first entry 
               counter += 1
          elif counter != 0:
               country_name = str(country.contents[3].text)
               total_countries.append(country_name)
     # print(len(total_countries)) #195
     return total_countries

response_countries = requests.get(COUNTRIES_URL)
html_countries = response_countries.content
soup_countries = BeautifulSoup(html_countries, 'html.parser')
all_countries = country_total(soup_countries) # list of all countries

response_GDP = requests.get(GDP_URL)
html_GDP = response_GDP.content
soup_GDP = BeautifulSoup(html_GDP, 'html.parser')

full_names = []
all_data = []
table = soup_GDP.find("tbody")
# print(table.contents[1].find('a').text)
for tr in table:
     my_tr = tr.find('a')
     if my_tr != -1:
          full_names.append(my_tr.text)
          print(my_tr.text)

     if isinstance(tr, NavigableString):
          continue
     if isinstance(tr, Tag):
          until_position = len(tr.contents[5].text)
          all_data.append(str(tr.contents[5].text[1:until_position - 1]))

# print(all_data)
data = {'Country': full_names, 
        'GDP' : all_data}

print(data)
#columns is selecting which part of dictionary to include, names have to be the same
df = pd.DataFrame(data, columns = ['Country', 'GDP']) 
df.to_csv('/Users/yimengwang/Documents/M2M/myproject/countries_webscraping/countryGDP_dataframe.csv', 
          index = False, header = True)

print(df)