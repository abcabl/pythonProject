import requests
from bs4 import BeautifulSoup
import time
url="https://www.umei.cc/bizhitupian/diannaobizhi/"
res=requests.get(url)
res.encoding="utf-8"
#print(res.text)
main_page=BeautifulSoup(res.text,"html.parser")
alist=main_page.find("div",class_="Clbc_Game").find_all("div",class_="item masonry_brick")
for i in alist:
    url1="https://www.umei.cc"+i.find("a").get("href")
    res1=requests.get(url1)
    res1.encoding="utf-8"
    main_page1=BeautifulSoup(res1.text,"html.parser")
    src1 = main_page1.find("div", class_="big-pic").find("a").find("img").get("src")
    print(src1)
#
#     image_=requests.get(src1)
#     image__name=src1.split("/")[-1]
#     with open("pictures/"+image__name,mode="wb")as f:
#         f.write(image_.content)
#     print("over...")
#     time.sleep(1)
# print("over!!")


