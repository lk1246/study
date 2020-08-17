import bs4
import json
import requests
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET

url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?"
servicekey= "zaE2F4LcLKhmszgOfK7XVaied0DMLxJTfVfIbwj9Q4rV3ZvkNNWoAXgWw9wouKsiciUUzKReu%2BiqXaYF5IQKmA%3D%3D"
LAWD_CD = input("지역코드: " )
DEAL_YMD = input("계약월: ")

parameter = "LAWD_CD=" + LAWD_CD + "&DEAL_YMD=" + DEAL_YMD + "&serviceKey=" + servicekey
result = requests.get(url + parameter)
print(result.url)
response = ET.fromstring(result.text)





"""
f= open("./sample.txt", 'w', encoding='utf-8')
for item in response.findall('body/items/item'):
    a = "아파트: {}, 전용면적: {}, 가격: {}".format(item.findtext("아파트"), item.findtext("전용면적"), item.findtext("거래금액"))
    f.write(a)
f.close()
"""
"""    
for item in response.findall('body/items/item'):
    print("아파트: {}, 전용면적: {}, 가격: {}".format(
        item.findtext("아파트"), item.findtext("전용면적"),item.findtext("거래금액")))
"""

s = pd.DataFrame()
for item in response.findall("body/items/item"):
    apt = item.findtext("아파트")
    cost = item.findtext("거래금액")
    width = item.findtext("전용면적")
    temp = pd.DataFrame(([[apt,cost, width]]), columns=["apt", "price", "width"])
    s = pd.concat([s, temp])
s.to_csv("s.csv", encoding='euc-kr')



"""
bs_obj = bs4.BeautifulSoup(result.content, 'html.parser')

for item in bs_obj.findAll("item"):
    print(item)
"""

