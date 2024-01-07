import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG, 
        format='[%(levelname)s](%(threadName)-10s) %(message)s')

def person():
    #print(threading.current_thread().getName(),"Starting")
    # https://stackoverflow.com/questions/69656020/printthreading-current-thread-getname-str-is-starting-n-why-is-the
    #print(threading.current_thread().name,"Starting")
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')
    #print(threading.current_thread().getName(),"Exiting")

def my_job():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exiting')
'''
    print(threading.current_thread().getName(),"Starting")
    time.sleep(3)
    print(threading.current_thread().getName(),"Exiting")
'''
t = threading.Thread(name='my_job', target=my_job)
w = threading.Thread(name='person', target=person)
w2= threading.Thread(target=person)

w.start()
w2.start()
t.start()
