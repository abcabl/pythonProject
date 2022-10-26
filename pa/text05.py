import requests
import re

url = "https://www.dytt89.com"
res = requests.get(url)
res.encoding = "gbk"
a = res.text
# print(res.text)
list=[]
obj = re.compile(r"2022必看热片.*?<ul>(?P<name>.*?)</ul>", re.S)
obj2=re.compile(r"<li><a href='(?P<http>.*?)'",re.S)
obj3=re.compile(r'◎片　　名(?P<name>.*?)<br.*?<!--xunleiDownList Start-->.*?<td style='
    r'"WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">magnet',re.S)
ret = obj.finditer(a)
for i in ret:
    b=i.group("name").strip()#截取一些小段
    ret2=obj2.finditer(b)#寻找网址
    for i in ret2:
        # print(i.group("http"))
        list.append(url+i.group("http"))#将网址存进数组里面
for i in list:
    r=requests.get(i)
    r.encoding="gbk"#改编码
    # print(r.text)
    ret3=obj3.search(r.text)
    a=ret3.group("name")

    b=ret3.group("download")
    print(f"{a}--------------->{b}")
    print("+++++++++++++")









