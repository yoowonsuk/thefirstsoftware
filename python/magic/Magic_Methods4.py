class X:
    def __init__(self,x):
        self.x = x

    def __mul__(self,other):
        return self.x * other.x
    def __add__(self,other):
        return self.x + other.x
    def __sub__(self,other):
        return self.x - other.x
    def __lt__(self,other):
        return self.x < other.x
    def __iadd__(self,other):
        self.x = self.x + other.x
        return self.x



obj1 = X(4)
obj2 = X(3)
print(obj1 * obj2)

obj1 += obj2
print(obj1) # obj1 += obj2 necessary
#print(obj1 += obj2)
