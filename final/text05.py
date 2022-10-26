num=eval(input("输入n的值"))#依据用户手动输入，任意输入5次数据即可
count=0
sum=0
for i in range(num,1,-1):
    sum=sum+i
    count=count+1
    for j in range(i):
        if j==0 or j==1:
            continue
        if i%j==0:
            sum=sum-i
            count=count-1
            break
    if count==10:
        break
if count==10:
    print(f"从[0,n]之间的最大的 10 个素数之和为：{sum}")
else:
    print("[0,n]之间的不存在最大的 10 个素数之和！")



