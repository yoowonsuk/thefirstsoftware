file = open('file1.txt', 'w') #'r' 'wb'
file.write('First text\n')
file.write('Second text')

content = """First text


Second test"""

'''
content = """
First text

Second text
'''

file.write(content)
file.close()


with open('file1.txt', 'w') as file:
    file.write()
    file.write()
    # file.close()

with open('file.txt', 'r') as file: # r is default
    content = file.read()
    

