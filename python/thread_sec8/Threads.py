import threading # high
#import _thread # low

def person(number):
    print("The Number is : %s" %number)
    return

threads=[]
for i in range(5):
    t = threading.Thread(target=person, args=(i,))
    threads.append(t)
    t.start()
