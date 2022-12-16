import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass

url='https://www.timeanddate.com/holidays/us/'
results= requests.get(url)
holiday= BeautifulSoup(results.text,'html.parser')

holiday_tr= holiday.find_all('tr')


# print(holiday_tr)

hol_th = holiday.find('th', {'class':'nw'})
print(hol_th.string)

