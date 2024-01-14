class A:
    def fun(self):
        print("A")

class B:
    def fun(self):
        print("B")

class C(A,B):
    def hello(self):
        #super().fun()
        A.fun(self)

obj1 = C()
obj1.hello()
obj1.fun()

# https://blog.hexabrain.net/286
