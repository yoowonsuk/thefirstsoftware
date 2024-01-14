# pickle => python structure
dictionary = {"Name":"Umair", "job":"tutorials", "company":"udemy"}

import csv

x = csv.writer(open("khan.csv","w"))
for key,val in dictionary.items():
    x.writerow([key,val])
