f=open("C:/Users/周银/Desktop/data.txt")
list=[]
for i in f.readlines():
    l=[]
    for j in i.strip().split(','):
        a=j.split(':')[1].strip()
        print(a)
        l.append(a)
    list.append(l)
print(list)
m=1
for i in list:
    sum=0
    for j in i:
        sum+=int(j)
    m=m+1
    print(f'第{m}行总和：{sum},平均值：{sum/len(i)}')


