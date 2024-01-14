class X(object):
    def __str__(self):
        return 'Hello World'

#print(str(X()))
print('Hello, %s ' %X())
