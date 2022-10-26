n = int(input("输入n的值："))
x1 = n
x2 = n
x3 = n
if n==1:
    print("不存在最大值！")
else:
    while (x1 + x2) % 2 != 0:
        x1 -= 1
    while (x2 + x3) % 3 != 0:
        x2 -= 1
    while (x1 + x2+x3) % 5 != 0:
        x3 -= 1
print(f"最大和：{x1+x2+x3}")

