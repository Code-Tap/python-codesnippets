import multiprocessing
import time

def mytask(num):
    print(f'Started task, sleeping {num}')
    time.sleep(num)

pool = multiprocessing.Pool(4)
jobs = pool.map_async(mytask, [1,2,3,4,5,3,2,3,4,5,2,3,2,3,4,5,6,4], chunksize=1)
pool.close()

while True:
    if not jobs.ready():
        print(f'We\'re not done yet, {jobs._number_left} tasks to go!')
        time.sleep(1)
    else:
        break