# Vanilla Methods
# Reverse Method
# In-Place Method

class X(object):
    def __init__(self,count):
        self._count = count

    def __add__(self, other):
        total_count = self._count + other._count
        return X(total_count)
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __iadd__(self, other):
        self._count = self._count + other._count
        return self._count
    def __str__(self):
        return 'Count: %i'%self._count

obj1 = X(3)
obj2 = X(4)
obj3 = obj1 + obj2 # x+y -> x+__add__(y)
print(obj3)

obj4 = 0 + obj1
print(obj4)

obj1 += obj2
print(obj1)
