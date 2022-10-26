import json
import time

from requests import post
from selenium.webdriver import Chrome
from selenium.webdriver.android import webdriver
from selenium.webdriver.common.keys import Keys

web=Chrome()
url="http://huyvum271-1.qty592.com/login.jsp?errno=13&url=http%3A%2F%2Fhuyvum271-1.qty592.com%2F"

web.get(url)
web.delete_all_cookies()
with open ('cookie.text',"r",encoding="utf-8")as f:
    listCookies=json.loads(f.read())
    for cookie in listCookies:
        cookie_dic={
            'domain':'.huyvum271-1.qty592.com',
            'name':cookie.get('name'),
            'value':cookie.get('value'),
            "expires":None,
            'path':'/',
            'httpOnly':False,
            'HostOnly':False,
            'sercure':False
        }
        web.add_cookie(cookie_dic)
   # print(cookie_dic)
time.sleep(3)
web.refresh()

