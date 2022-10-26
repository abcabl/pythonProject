import json
from asyncio import sleep

import requests
from requests import post
from selenium.webdriver import Chrome
from selenium.webdriver.android import webdriver
from selenium.webdriver.common.keys import Keys

web=Chrome()
web.get("http://huyvum271-1.qty592.com/login.jsp?errno=13&url=http%3A%2F%2Fhuyvum271-1.qty592.com%2F")
web.find_element_by_xpath('//*[@id="memberLoginAcct"]/input').send_keys("18725174330")
web.find_element_by_xpath('//*[@id="memberLoginPwd"]/input').send_keys("123123",Keys.ENTER)
# web.get("http://huyvum271-1.qty592.com/login.jsp?errno=13&url=http%3A%2F%2Fhuyvum271-1.qty592.com%2F")
cookie_items=web.get_cookies()
jsoncookies=json.dumps(cookie_items)
with open('cookie.text','w')as f:
    f.write(jsoncookies)
print("over!")
#获取token的方法：
''' 
1、要从Local Storage中获取还是要从Session Storage中获取，具体看目标系统存到哪个中-----开发者模式查看
2、window.SessionStorage和直接写SessionStorage是等效的
3、一定要使用return，不然获取到的一直是None
4、get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
'''































