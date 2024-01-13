import os
path = "umair.txt"

file = open(path, "w+") # r w x(create) a b t +r w+   =>   default read mode
#file = open(path, "r") # r w x(create) a b t +r w+   =>   default read mode
#file = open(path, "a") # r w x(create) a b t +r w+   =>   default read mode
file.write("Umair Kham")
file.write("Make cool tuturials")
#data = file.read()
#print(data)
file.close()

#os.rename("umair.txt", "umair_khan.txt")
