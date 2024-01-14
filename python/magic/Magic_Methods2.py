class X:
    def __init__(self, value):
        self._value = value

    def __pos__(self):
        print('pos magic method is called')
        return (+self._value)
    def __neg__(self):
        print('neg magic method is called')
        return (-self._value)
    def __invert__(self):
        return self._value[::-1]
    def __str__(self):
        return self._value



obj1 = X(3)
#print(+obj1)
print(-obj1)

obj2 = X('Hello World')
inv_obj = ~obj2
print(inv_obj)
