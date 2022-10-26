import re
import requests
import csv
url = "https://movie.douban.com/chart"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53"}
res = requests.get(url, headers=headers)
print("----------------------------")
# print(res.text)
a = res.text

# obj = re.compile(r'<div class="pl2">.*?class="">(?P<name>.*?)/', re.S)
# obj=re.compile(r'<div class="pl2">.*?>(?P<name>.*?)/',re.S)
# obj2=re.compile(r'<span class="pl">(?P<num>.*?)<',re.S)
# obj3=re.compile(r'<p class="pl">(?P<age>.*?)/',re.S)
# obj4=re.compile(r'<p class=.*?/.*?/(?P<people>.*?)<',re.S)
obj5 = re.compile(r'<div class="pl2">.*?>(?P<name>.*?)/'
                  r'.*?<p class="pl">(?P<age>.*?)/'
                  r'.*?<span class="pl">(?P<num>.*?)</', re.S)
ret = obj5.finditer(res.text)
f=open("data.csv",mode="w")
csvwriter=csv.writer(f)

for i in ret:
    # print(i.group("name").strip())
    # print(i.group("age"))
    # print(i.group("num"))
    # print("________________")
    dic=i.groupdict()
    dic["name"]=dic["name"].strip()
    csvwriter.writerow(dic.values())
f.close()
print("over")
