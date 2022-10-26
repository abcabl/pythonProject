id=input("请输入18位身份证号:")
sum=int(id[0])*7+int(id[1])*9+int(id[2])*10+int(id[3])*5+int(id[4])*8+int(id[5])*4+int(id[6])*2+int(id[7])*1+int(id[8])*6+int(id[9])*3+int(id[10])*7+int(id[11])*9+int(id[12])*10+int(id[13])*5+int(id[14])*8+int(id[15])*4+int(id[16])*2
a=sum%11
if id[17]!='X':
    b = int(id[17])
else:
    b=id[17]

if a==0 and b==1:
    print("身份证号码校验为合法号码！")
elif a==1 and b==0:
    print("身份证号码校验为合法号码！")
elif a==2 and b=='X':
    print("身份证号码校验为合法号码！")
elif a==3 and b==9:
    print("身份证号码校验为合法号码！")
elif a==4 and b==8:
    print("身份证号码校验为合法号码！")
elif a==5 and b==7:
    print("身份证号码校验为合法号码！")
elif a==6 and b==6:
    print("身份证号码校验为合法号码！")
elif a==7 and b==5:
    print("身份证号码校验为合法号码！")
elif a==8 and b==4:
    print("身份证号码校验为合法号码！")
elif a==9 and b==3:
    print("身份证号码校验为合法号码！")
elif a==10 and b==2:
    print("身份证号码校验为合法号码！")
else:
    print("身份证校验位错误!")








