import numpy as np
import matplotlib.pyplot as plt
#设置图片大小为300*300，但是在此函数里长宽都要/100!!!
plt.figure(figsize=(4,4))
#np.arange，约等于range函数
x=np.arange(-3,2*np.pi,0.1)#np.pi=3.141592653589793
y=np.sin(x)
y_1=np.cos(x)
plt.plot(x,y,'r')
plt.plot(x,y_1,'b--')
#理论上来说让matplotlib显示几万条都没问题
plt.show()#显示函数图像
