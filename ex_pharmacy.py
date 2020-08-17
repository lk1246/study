import bs4
import json
import requests
import pandas as pd
import numpy as np
from urllib.parse import quote


endpoint =  'http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?'
servicekey= "zaE2F4LcLKhmszgOfK7XVaied0DMLxJTfVfIbwj9Q4rV3ZvkNNWoAXgWw9wouKsiciUUzKReu%2BiqXaYF5IQKmA%3D%3D"
Q0= quote("서울특별시")
Q1 = quote("강남구")
QT="1"
QN=quote("삼성약국")
ORD = 'NAME'
pageNo="1"
numOfRows = "10"

parameter = "serviceKey=" + servicekey +"&Q0=" + Q0 + "&Q1=" + Q1 + "&QT=" + QT + "&QN=" + QN + "&ORD=" + ORD + "&pageNo=" + pageNo + "&numOfRows=" + numOfRows
url = endpoint + parameter

print("url: " + url)
result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, 'html.parser')
for item in bs_obj.findAll("item"):
    print(item)

for item in bs_obj.findAll('item'):
    taged_name = item.find('dutyname')
    print(taged_name.text)

print("___________________________________")
print()
"""
서울에 있는 모든 약국을 검색해서 확인
"""

parameter_1 = "serviceKey=" + servicekey +"&Q0=" + Q0 + "&ORD=" + ORD + "&pageNo=" + pageNo + "&numOfRows=" + numOfRows
url_1 = endpoint + parameter_1

result = requests.get(url_1)
bs_obj = bs4.BeautifulSoup(result.content, 'html.parser')
for item in bs_obj.findAll("item"):
    store = item.find("dutyname")
    print(store.text)

print("url:" + url_1)

"""
서울에서 9시 이후까지 하는 약국 검색
"""

numOfRows_1 = "5000"
parameter_2 = "serviceKey=" + servicekey +"&Q0=" + Q0 + "&ORD=" + ORD + "&pageNo=" + pageNo + "&numOfRows=" + numOfRows_1
url_2 = endpoint + parameter_2

result_2 = requests.get(url_2)
bs_obj_2 = bs4.BeautifulSoup(result_2.content, "html.parser")

count = 0
for item in bs_obj_2.findAll('item'):
    target_time = item.find('dutytime1c')
    if (target_time != None):
        close_time = int(target_time.text)
        if close_time >2100:
            count += 1

print("월요일 9시 이후까지 하는 약국" + str(count))