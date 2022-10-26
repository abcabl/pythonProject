import requests
import  csv
from lxml import etree
f=open("猪八戒网.csv",mode="w")
csvwriter=csv.writer(f)
url="https://hefei.zbj.com/search/service/?kw=saas&r=1&nt=3606&fcn=%E7%94%B5%E5%AD%90%E5%95%86%E5%9F%8E%E7%B3%BB%E7%BB%9F"
resp=requests.get(url)
#print(resp.text)
html=etree.HTML(resp.text)
divs=html.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div')
for div in divs:
    price=div.xpath('./div/div[3]/div[1]/span/text()')
    print(price[0])
    title=div.xpath('./div/div[3]/a/text()')
    print("sasa".join(title))
    review=div.xpath('./div/div[3]/div[2]/div[1]/span[2]/text()')
    _review=0;
    if(len(review)==0):
        print(f"好评数:0")
    else:
        print(f"好评数:{review[0]}")
        _review=review[0]
    goodman=div.xpath('./div/div[2]/a/div[2]/div[4]/span[2]/text()')
    _goodman=None
    if (len(goodman) == 0):
        print(f"人才所在地:无")
        _goodman="无"
    else:
        print(f"人才所在地:{goodman[0]}")
        _goodman=goodman[0]
    s1="价格-->"+str(price[0].strip("￥"))
    s2="项目名称-->"+"sasa".join(title)
    s3="评论数-->"+str(_review)
    s4="人才所在地-->"+_goodman
    csvwriter.writerow([s1, s2, s3, s4])
resp.close()


