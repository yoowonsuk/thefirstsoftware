def table(n):
    result = n*4
    #return result
    yield result
    yield n*5
    yield n*6

a = table4(3)
#print(a)
print(a.__next__())
print(a.__next__())
print(next(a))
