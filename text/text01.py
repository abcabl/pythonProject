


class A:
    name=None;
    def __init__(self,name):
        self.name=name
    def text(self):
        print("A类的函数")
class B(A):
    age=0
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def text(self):
        print("B的函数")
    def A_text(self):
        super().text()
class C(B):
    sex=None
    def __init__(self,name,age,sex):
        super().__init__(name,age)
        self.sex=sex
    def text(self):
        print("C的函数")
    def B_text(self):
        super().A_text()
c=C("张三",19,"男")
c.text()
c.B_text()
b=B("李四",12)
b.text()
b.A_text()




