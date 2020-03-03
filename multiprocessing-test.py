'''
https://stackoverflow.com/questions/36962462/terminate-a-python-multiprocessing-program-once-a-one-of-its-workers-meets-a-cer
'''

import random
import multiprocessing as mp
from time import sleep

def worker(i, quit, foundit):
    print(f'{i} started')
    while not quit.is_set():
        x = random.random()
        if x > 0.9:
            print(f'{i} found {x}')
            foundit.set()
            break
        sleep(0.1)
    print(f'{i} is done')

if __name__ == '__main__':
    quit = mp.Event()
    foundit = mp.Event()
    for i in range(mp.cpu_count()):
        p = mp.Process(target=worker, args=(i, quit, foundit))
        p.start()
    foundit.wait()
    quit.set()