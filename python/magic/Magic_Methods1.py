class X:
    def __new__(cls):
        print("Statement in the New Magic Method")
        inst = object.__new__(cls)
        return inst
    def __init__(self):
        print("This is the constructor function")
        self.name = "John"
    def __del__(self):
        print("Desturctor method called")



obj1 = X()
#del obj1
