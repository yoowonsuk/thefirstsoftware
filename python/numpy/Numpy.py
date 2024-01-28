import numpy as np

a1 = np.array([2,5,8,9,2,9,0,1,5])
print(a1)
#print(a1[2])
print(a1[-1])
print(a1.size)
print(a1.itemsize) # 8 byte each data *8 => bits
print(a1.nbytes) #8*9=72 8* => bits
print(a1.dtype) #int64

a2 = np.array([[3,6,1,9],[4,7,9,1],[3,9,8,5]]) # column size should be same in each row
print(a2)
print(a2.ndim)
print(a2.shape)
print(a2.size)
print(a2.dtype)
print(a2.itemsize) # *8 => bits
print(a2.nbytes)

print("\n")
#print(a1+1)
#print(2**a2)
#print(a1[0:4]) # a[:4] a[0::2] a[0::-2]
print(a2[:2, :2])
print(a2[0, :]) # a2[:,0] all row, first column

b = np.array([3,1,9,1,5,7,5,4,3,1,11], dtype=float) # dtype=float
print(np.zeros([3,4],  dtype=int))
print(np.ones([3,4], dtype=str))

c = np.arange(5,70,4)
print(c)
d = np.linspace(3,5,9)
print(d)

e = np.array([3,9,1,5,7,9]).reshape(2,3)
print(e)
f = np.reshape(e,(2,3))
g = np.arange(1,9,1)
h = np.concatenate([a1,g])
print(h)
