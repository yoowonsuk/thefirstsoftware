x = list(map(lambda x:x, 'Hello'))
print(x)

op = open("python.txt", "r")
output = [ i for i in op if "what" in i]
print(output)

def y(a):
    return a*2

print([y(a) for a in range(10) if a%2==0])
#print(y(a) for a in range(10))
