
import csv
import numpy as np

list=[]
dic={}
list2=[]
dic2={}
print("将‘室’改为‘房间’,并数据设置为 np.float64 数据类型结果如下：------------")
with open('C:\\Users\\周银\\Desktop\\期末考试题目-21-学生\\zfsj.csv', encoding='utf-8-sig') as f:
    for row in csv.reader(f):
        if row[3]=='面积(㎡)':
            print(row)
            continue
        num=np.float64(float(row[3].replace('平米','')))#去掉平米单位并设置该列数据为 np.float64 数据类型
        row[3]=num


        row[2]=row[2].replace("室","房间")#将“室”改为“房间”

        print(row)
        list.append(row[0])#统计区域数量
        list2.append(row[2])#统计户型
print("统计区域数量如下：------------------")#-------------------------------
for i in list:#统计区域数量
    dic[i]=list.count(i)
print(dic)
list1=[]
list1.append(" ")
list1.append("区域")
list1.append("数量")
print(list1)
a=0
for i in dic.keys():
    list1.clear()
    list1.append(a)
    list1.append(i)
    list1.append(dic[i])
    print(list1)
    a=a+1

_dic={}#将字典中键值互换
for i in list2:#统计区域数量
    if list2.count(i)>50:
        dic2[i] = list2.count(i)

_list=[]#将字典中的值存储在该列表中，以便后续排序
for key,value in dic2.items():
    _dic[value]=key
    _list.append(value)
_list.sort(reverse=True)

s='  '+'户型'+'     '+'数量'

with open(' zfsj4_after.csv','w') as f:
    f.write(s+'\n')
    count=0
    for i in _list:
        s=str(count)+' '+_dic[i]+' '+str(i)
        f.write(s+'\n')
        count=count+1#将排序结果写入csv文件中去









