name = input("请输入用户名：")
sword = input("请输入密码：")
if name != "aaa" and name != "bbb" and name != "ccc":
    print("wrong user!")
else:
    if ((name == "aaa" and sword != "123456") or (name == "bbb" and sword != "888888") or (
            name == "ccc" and sword != "333333")):
        print("fail!")
    else:
        print("success!")
