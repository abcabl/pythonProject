import matplotlib.pyplot as plt
import requests
from lxml import etree
import numpy as np
from pyecharts.charts import Bar
from pyecharts import options as opts

url="https://www.jd.com/chanpin/148470.html"
resp=requests.post(url).text
html=etree.HTML(resp)
divs=html.xpath('//*[@id="J_goodsList"]/ul')
for div in divs:
    price=div.xpath('./li/div/div[3]/strong/i/text()')
    # print(price)#价格
    count=div.xpath('./li/div/div[5]/strong/a/text()')
    # print(count)#评论数
    name=div.xpath('./li/div/div[4]/a/em/text()')#拿到书名或简介


l_name=[]
for i in name:
    l_name.append(i.split(" ")[0].split("（")[0].split("：")[-1])#通过字符串切割拿到想要的书名
# print(l_name)#书名
_x = np.arange(len(l_name))  # 获得长度并生成数组
width = 0.2


_count=[]#存储数字形式的评论数
for i in count:
    _count.append(float(i)/10000)
# print(_count)
_price=[]
for i in price:
    _price.append(float(i))

bar=Bar(init_opts=opts.InitOpts(width="1600px",
                                height="750px"))
bar.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=15,interval=0)))
bar.add_xaxis(l_name)
bar.add_yaxis("价格(元)",_price)
bar.render('mycharts1.html')#保存“书名-价格”

bar2=Bar(init_opts=opts.InitOpts(width="1600px",
                                height="750px"))
bar2.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=15,interval=0)))#设置文字旋转角度
bar2.add_xaxis(l_name)
bar2.add_yaxis("评论数(万次)",_count)
bar2.render('mycharts2.html')#保存“书名-评论数”
