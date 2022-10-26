ip = input("请输入一个人ip地址：")
a = ip.split(".")
fag=True
if len(a) != 4:
    print("no")
else:
    if 0 <= int(a[0]) <= 255:
        for i in range(4):
            if int(a[i]) > 255 or int(a[i]) < 0:
                fag=False
                break
        if not fag:
            print("no")
        else:
            print("yes")
    else:
        print("no")

