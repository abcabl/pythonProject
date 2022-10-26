try:
    num=eval(input("请输入为 24 小时 PM2.5 平均值标准值"))
    if 0<=num<35:
        print("优")
    elif 35<=num<75:
        print("良")
    elif 75<=num<115:
        print("轻度污染")
    elif 115<=num<150:
        print("中度污染")
    elif 150<=num<250:
        print("重度污染")
    else:
        print("严重污染")
except:
    print("输入数值有误")
