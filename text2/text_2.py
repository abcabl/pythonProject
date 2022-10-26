import json
_list=[]
with open("C:/Users/周银/Desktop/score1034.json",encoding="utf-8")as f:
    a=json.load(f)
    # print(a)
    for i in a:
        _list.append(list(i.keys()))
        _list.append(list(i.values()))
# print(_list)
n=input("输入一个数字n:")
for i in range(int(n)):
    print(_list[i])
