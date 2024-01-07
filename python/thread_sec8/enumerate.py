import logging
import threading
import time
import random

logging.basicConfig(level=logging.DEBUG, 
        format='[%(levelname)s](%(threadName)-10s) %(message)s')

def person():
    t = threading.current_thread()
    pause = random.randint(1,5)
    logging.debug('sleeping %s', pause)
    time.sleep(pause)
    logging.debug('Ending %s', t.getName())
    return

for i in range(3):
    t = threading.Thread(target=person)
    t.setDaemon(True)
    t.start()

main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    logging.debug(('Joining %s', t.getName()))
    t.join()
