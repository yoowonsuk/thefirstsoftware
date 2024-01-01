feh = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}
cel = list(map(lambda x: (float(5)/9)*(x-32),feh.values()))
cel_dict = dict(zip(feh.keys(), cel))
print(cel_dict)

cel_dict = {k:(float(5)/9)*(v-32) for (k,v) in feh.items()}
print(cel_dict)

dicts = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}
#new_dict = {k:v for (k,v) in dicts.items() if v>3}
#new_dict = {k:('even No' if v%2==0 else 'odd NO') for (k,v) in dicts.items()}
new_dict = {k:v for (k,v) in dicts.items() if v>3 if v%2==0}
print(new_dict)

dicts = {'one':{'a':10}, 'two':{'b':20}} # nested dictionary
for (external_key, external_value) in dicts.items():
    for (internal_key, internal_value) in external_value.items():
        external_value.update({internal_key: float(internal_value)})

# dicts.update({external_key:external_value}) # duplicate
print(dicts)
