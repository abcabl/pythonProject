n = int(input("输入n的值："))
sum = 0
for i in range(n):
    a=i+1
    min = 0
    for j in range(a):
        min = min * 10 + j+1
    sum += min
print(f"结果为{sum}")
