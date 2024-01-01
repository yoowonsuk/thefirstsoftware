num = [1,2,3,4,5]
squares = []

for n in num:
    if(n%2==0): # if (not (n%2))
        squares.append(n**2)

print(squares)

# squares = [ n**2 for n in num if n % 2 == 0 ] 

list = [1,2,3,4,5]
list1 = [2,3,4,5,6]

intersection = []
for x in list:
    for y in list1:
        if x==y:
            intersection.append(x)

print(intersection)

# intersection = [ x for x in list for y in list1 if x==y ]
# non_common_elemets = [ (x, y) for x in list for y in list1 if x!=y ]

list = ['Hello World', 'Python', 'java', 'C']
x = [str.lower() for str in list]
print(x)

list = [1,2,3,4,5]
x = [[a**2, a**3] for a in list]
print(x)

# Ctrl + shift + f10
