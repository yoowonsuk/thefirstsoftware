dictionary = {"Name":"Umair", "job":"tutorials", "company":"udemy"}

import json

json = json.dumps(dictionary)
x = open("umair.json", "w")
x.write(json) # or just x.write(str(dictionary))
x.close()

