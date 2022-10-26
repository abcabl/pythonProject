a=input("输入3个正整数,以逗号分割:")
b=a.split(",")
c=[]
#print(b)
for i in range(int(b[2])):
    c.append(int(b[0])+i*int(b[1]))
print(c)




