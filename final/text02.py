import numpy as np
import matplotlib
import matplotlib.pyplot as plt
f=open("C:\\Users\\周银\Desktop\\期末考试题目-21-学生\\期末考试题目-21-学生\\sensor-data.txt")
list=[]
time=[]
tempture=[]
shi=[]
light=[]
dian=[]
matplotlib.rc('font',family='Microsoft YaHei')
plt.figure(figsize=(10, 7))
for i in f.readlines():
   num=float(i.split(" ")[4])
   list.append(num)
   time.append(i.split(' ')[1])
   tempture.append(float(i.split(' ')[2]))
   shi.append(float(i.split(' ')[3]))
   light.append(float(i.split(' ')[4]))
   dian.append(float(i.split(' ')[5]))
mean=np.mean(list)#求均值
std=np.std(list)#求标准差
max=max(list)
min=min(list)
print(f"最大值-->{round(max,2)}")
print(f"最小值-->{round(min,2)}")
print(f"均值-->{round(mean,2)}")
print(f"标准差-->{round(std,2)}")
#时间-温度图如下：
plt.subplot(2,2,1)
plt.plot(time,tempture,color='r',linestyle=':')
plt.tick_params(axis='both',labelsize=6)
plt.xticks(rotation=45)
plt.xlabel(xlabel='时间',fontsize=8)
plt.ylabel(ylabel='温度',fontsize=8)
plt.title("时间-温度")

# 时间-湿度图如下：
plt.subplot(2,2,2)
plt.plot(time,shi,color='g',linestyle='--')
plt.tick_params(axis='both',labelsize=6)
plt.xticks(rotation=45)
plt.xlabel(xlabel='时间',fontsize=8)
plt.ylabel(ylabel='湿度',fontsize=8)
plt.title("时间-湿度")

#时间-光照图如下：
plt.subplot(2,2,3)
plt.plot(time,light,linestyle='-.')
plt.tick_params(axis='both',labelsize=6)
plt.xticks(rotation=45)
plt.xlabel(xlabel='时间',fontsize=8)
plt.ylabel(ylabel='光照',fontsize=8)
plt.title("时间-光照")

#时间-电压图如下：
plt.subplot(2,2,4)
plt.plot(time,dian,color='b')
plt.tick_params(axis='both',labelsize=6)
plt.xticks(rotation=45)
plt.xlabel(xlabel='时间',fontsize=8)
plt.ylabel(ylabel='电压',fontsize=8)
plt.title("时间-电压")
plt.tight_layout()#防止图像有重叠部分


plt.show()



