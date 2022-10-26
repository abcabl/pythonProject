import csv

from bs4 import BeautifulSoup
import requests

url = "http://zhongdapeng.com/shucaijiage/1103.html"
res = requests.get(url)
res.encoding = "utf-8"  # 获得页面
f=open("菜价.csv",mode="w")
csvwriter= csv.writer(f)
#print(res.text)
page = BeautifulSoup(res.text, "html.parser")
table=page.find("table",cellspacing="0", width=436)
#print(table)
trs=table.find_all("tr")[1:]
for i in trs:
    tds=i.find_all("td")
    name=tds[0].text.strip()
    price=tds[1].text.strip()
    num=tds[2].text.strip()
    csvwriter.writerow([name,price,num])
f.close()
print("over")

