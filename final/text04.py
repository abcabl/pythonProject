import math
AB=eval(input("输入弦长AB"))
CD=eval(input("输入弓高CD"))
AO=AB**2/(8*CD)+CD/2#半径表达式
print(f"该圆的半径为：{round(AO,2)}")
AOB= 2 * math.asin(AB/2.0/AO)#角度
Saobc=0.5*AOB*AO**2#扇形面积
Saob=0.5*math.sin(AOB)*AO**2#三角形面积
S=Saobc-Saob
print(f"弓形 ABC 的面积为：{round(S,2)}")




