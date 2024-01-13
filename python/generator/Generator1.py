def natural_No(n):
    result = []
    for i in range(1, n):
        #result.append(i)
        yield(i)
    #return result
n = natural_No(10)
#print(n)
#print(next(n))
#print(n.__next__())
for i in n:
    print(i)


