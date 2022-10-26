father=int(input("父亲身高（cm)："))
mother=int(input("母亲身高(cm)："))
sex=input("性别：")
if sex!="男"and sex!="女":
    print("无对应公式！")
else:
    if sex=="男":
        print(f"身高：{int((father+mother)*1.08/2)}")
    else:
        print(f"身高：{int((father*0.923 + mother) / 2)}")

