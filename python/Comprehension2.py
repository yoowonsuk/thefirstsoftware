dict = {'a':1, 'b':2, 'c': 3, 'd':4}
x = dict.keys()
print(x)

y=dict.values()
print(y)

z=dict.items()
print(z)

new_dict_values = {k:v*2 for (k,v) in dict.items()}
print(new_dict_values)

new_dict_keys = {k*2: v for (k,v) in dict.items()}
print(new_dict_keys)

dict = {}
for i in range(10):
    if i%2 == 0:
        dict[i]=i**2

#print(dict)

dict = {i:i**2 for i in range(10) if i % 2 == 0}
print(dict)
