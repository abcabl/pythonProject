dict1 = {'赵广辉': '13299887777', '特朗普': '814666888', '普京': '522888666', '吴京': '13999887777'}
name = input("请输入姓名:")
if dict1.get(name) is None:
    print("数据不存在")
else:
    print(dict1.get(name))

