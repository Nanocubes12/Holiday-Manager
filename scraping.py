import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass

url='https://www.timeanddate.com/holidays/us/'
results= requests.get(url)
holiday= BeautifulSoup(results.text,'html.parser')

holiday_table= holiday.find_all('table')
print(holiday_table)
# <table id="holidays-table" 