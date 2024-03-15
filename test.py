import requests
import pyzard
import json
import time
# headers = {
#     'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Cache-Control': 'max-age=0', 
#     'Referer': 'https://search.naver.com/search.naver?ie=UTF-8&query=%ED%86%A0%EB%A7%88%ED%86%A0&sm=chr_hty',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
# }
# url = "https://search.shopping.naver.com/search/all?where=all&frm=NVSCTAB&query=%ED%86%A0%EB%A7%88%ED%86%A0"

# # HTTP GET 요청 보내기
# response = requests.get(url,headers=headers).text
# t = pyzard.pinset(response,'"total":',',')
# print(t)
def generate(self,timestamp, method, uri, secret_key):
    message = "{}.{}.{}".format(timestamp, method, uri)
    #hash = hmac.new(bytes(secret_key, "utf-8"), bytes(message, "utf-8"), hashlib.sha256)
    hash = hmac.new(secret_key.encode("utf-8"), message.encode("utf-8"), hashlib.sha256)
    hash.hexdigest()
    return base64.b64encode(hash.digest())

BASE_URL = 'https://api.naver.com'
API_KEY = "0100000000621aae65a5a7d651ffcb463d89f74a27d08e61f26fa4514be999d771a0cdfb99"
SECRET_KEY ="AQAAAABiGq5lpafWUf/LRj2J90onCrj+bzbfcT48VD4z9PX9JA=="
CUSTOMER_ID = "1538797"
def get_header(method, uri, api_key, secret_key, customer_id):
    timestamp = str(int(time.time() * 1000))
    signature = generate(timestamp, method, uri, SECRET_KEY)
    return {'Content-Type': 'application/json; charset=UTF-8', 'X-Timestamp': timestamp, 'X-API-KEY': self.API_KEY, 'X-Customer': str(self.CUSTOMER_ID), 'X-Signature': signature}
dic_return_kwd = {}
naver_ad_url = '/keywordstool'
#_kwds_string = '원피스' #1개일경우
#_kwds_string = ['나이키', '원피스', '운동화'] #키워드 여러개일경우
method = 'GET'
prm = {'hintKeywords' : '감자' , 'showDetail':1}
#    ManageCustomerLink Usage Sample
r = requests.get(BASE_URL + naver_ad_url, params=prm, headers=get_header(method, naver_ad_url, API_KEY, SECRET_KEY, CUSTOMER_ID))

key_id = json.loads(r.text)


array = key_id['keywordList']
print(array)
