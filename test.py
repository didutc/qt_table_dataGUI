import webbrowser

import pyperclip
from ast import keyword
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import pickle
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from functools import partial
import requests
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from os import environ       
import requests
import time
import  hmac
import  hashlib
import  base64
import json
import doubleagent

def generate(timestamp, method, uri, secret_key):
    message = "{}.{}.{}".format(timestamp, method, uri)
    #hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
    hash = hmac.new(secret_key.encode("utf-8"), message.encode("utf-8"), hashlib.sha256)
    hash.hexdigest()
    return base64.b64encode(hash.digest())


def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(int(time.time() * 1000))
    signature = generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': API_KEY, 'X-Customer': str(CUSTOMER_ID), 'X-Signature': signature}

keyword = '돼지고기'
keyword=keyword.upper()
dic_return_kwd = {}
naver_ad_url = '/keywordstool'
#_kwds_string = '원피스' #1개일경우
#_kwds_string = ['나이키', '원피스', '운동화'] #키워드 여러개일경우
method = 'GET'
prm = {'hintKeywords' : keyword , 'showDetail':1}
#    ManageCustomerLink Usage Sample
r = requests.get(BASE_URL + naver_ad_url, params=prm, headers=get_header(method, naver_ad_url, API_KEY, SECRET_KEY, CUSTOMER_ID))

key_id = json.loads(r.text)


array = key_id['keywordList']
naver_lst_lst = []
for li in array:
    try:
        relkeyword = li["relKeyword"]

        viewcount = int(li["monthlyPcQcCnt"])+int(li["monthlyMobileQcCnt"])

        if viewcount < 300:
            continue
        key_lst =[relkeyword,str(viewcount)]
        naver_lst_lst.append(key_lst)
    except:

        continue
naver_lst_lst=sorted(naver_lst_lst, key=lambda key_lst: int(key_lst[1]),reverse=True)

print(naver_lst_lst)
keyword = {'keywords': i}

# print(array[0])
Url = 'https://api.itemscout.io/api/keyword/data/list'
res = requests.post(Url, data=keyword)
json_val = json.loads(res.text)
array = json_val['data']
i = 1

for li in array:
    try:

        name = li['keyword']
        bid = li['bid']
        pc_bid = bid['pc_bid']
        mobile_bid = bid['mobile_bid']
        prdCnt = li['prdCnt']
        monthly = li['monthly']
        total = monthly['total']
        average = prdCnt/total
        name_array.append(name)
        pc_bid_array.append(pc_bid)
        mobile_bid_array.append(mobile_bid)
        total_array.append(total)
        average_array.append(average)
        prdCnt_array.append(prdCnt)

    # print(li['prdCnt'])
    # print(clicka['total'])
    # print(li['bid'])
    except:
        continue
time.sleep(0.5)
print(len(name_array))
print(len(prdCnt_array))
print(len(total_array))
print(len(average_array))
print(len(pc_bid_array))
print(len(mobile_bid_array))