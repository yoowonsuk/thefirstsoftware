import os
import shutil
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
#os.remove("umair.csv")
#os.rmdir("umair.csv")
shutil.rmtree("khan") # recursive

with open(path,"w") as file:
    file.write("Umair Khan")
file.write("Is it Opened") # not work

# pickle => python structure
dictionary = {"Name":"Umair", "job":"tutorials", "company":"udemy"}

import csv

x = csv.writer(open("khan.csv","w"))
for key,val in dictionary.items():
    x.writerow([key,val])
