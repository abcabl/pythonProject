# //*[@id="float_img_610"]
# //*[@id="float_img_610"]
# //*[@id="float_img_612"]
# //*[@id="float_img_602"]
import json
import urllib
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
# lists=web.find_elements_by_xpath( '//*[@id="fullmeasureTopForms"]/div')
# print(web.find_element_by_xpath('//*[@id="float_img_602"]').get_attribute("data-original"))
# for list in lists:
#     a=list.find_element_by_xpath('./div[2]/div[2]/div/div[2]/div[2]/div/div/a/div/div/img')
#     print(a.get_attribute("data-original"))
# print(web.find_elements_by_tag_name("img")[0].get_attribute("data-original"))
print(web.page_source)