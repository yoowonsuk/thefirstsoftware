dictionary = {"Name":"Umair", "job":"tutorials", "company":"udemy"}

import pickle

x = open("umair.pkl", "wb")
pickle.dump(dictionary,x)
x.close()
