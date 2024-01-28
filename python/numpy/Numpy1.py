import  numpy as np
a =np.array([2,5,6,1])
b =np.array([3,5,3,7])
print(a==b)

c = np.arange(1,10)
d = np.arange(1,10)
print(np.array_equal(a,b))
print(np.array_equal(c,d))

print(np.logical_or(a,b))
print(np.logical_and(a,b)) # xor not

e = np.linspace(0,2,9)
print(e)

print(np.cos(e)) # np.sin, np.tan np.arcsin

f = np.array([-1,-4,7,6,4,3,-9])
g = np.array([3,6,1,2,8,9,1])
print(np.add(f,g)) #np.abs(a)
print(np.power(g,3))
print(np.log2(g))
print(np.log10(g))
print(np.add.reduce(g)) # reduce to addition
print(np.multiply.reduce(g))
print(np.multiply.accumulate(g))
print(np.max(f)) # np.min np.argmin np.sqrt np.append(g,[100,200,300])
big_data = np.random.random_integers(1,101,1000)
print(big_data)

