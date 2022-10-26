import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.keys import Keys

#浏览器模式设置
chrome_options=Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome()#用selenium模拟登录，并借助driver.execute_script拿到token
url = "https://pic.kontori.top/login"


def get_token():#获得token的函数
#操作浏览器，打开url，用户名密码登陆
    driver.get(url)
    a=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div/input')
    a.clear()#清空name文本框，防止原来文本框中有信息
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[1]/div/div/input').send_keys("zbc123")
    b=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input')
    b.clear()#清空password文本框，防止原来文本框中有信息
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/div/div/input').send_keys("123",Keys.ENTER)
    time.sleep(5)#休眠，防止操作过快
    token = driver.execute_script('return localStorage.getItem("token");')
    driver.close()
    return token
token=get_token()
url='https://pic.kontori.top/api/getAllCollections?'+'token='+token+'&page=1&limit=15&mode=1'#拼接出正确的地址
resp=requests.get(url)
resp.encoding="utf-8"
info=resp.json()#转为字典
download=info["data"]
for i in download:
        id=i["collectionId"]
        name=i["name"]
        artist=i["artist"]
        imgurl=i["imgUrl"]
        resp2=requests.get(imgurl)
        img_name=str(id)+"-"+name+"-"+artist+"."+imgurl.split("?")[0].split(".")[-1]
        with open('C:/Users/周银/Desktop/getAllCollections/'+img_name,mode="wb")as f:
            f.write(resp2.content)
            print("over...")
print("all over !")



