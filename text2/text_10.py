a=int(input("输入n的值"))
for i in range(a+1):
    flg = 0
    if i==0 or i==1:
        continue
    for j in range(i):
        if j==0 or j==1:
            continue
        if i%j==0:
            flg=1
            break
    if flg==0:
        print(i)






