from pathlib import Path

'''
p1 = 'files/abc.txt'

with open(p1, 'r') as file:
    print(file.read())
'''

p1 = Path('files/abc.txt')
print(type(p1)) # <class 'pathlib.PosixPath'>

if p1.exists() #dir(Path)
    with open(p1, 'r') as file:
        print(file.read())

if not p1.exists():
    with open(p1, 'w') as file:
        file.write('Content 3')

print(p1.name)
print(p1.stem) #ghi
print(p1.suffix) # .txt

p2 = Path('files')
#print(p2.iterdir())
print(list(p2.iterdir()))
for item in p2.iterdir():
    print(type(item)) # print(item)
