from multiprocessing import Pool, TimeoutError

def FizzBuzz(x):
    msg = ''
    if x % 3 == 0: msg += 'Fizz'
    if x % 5 == 0: msg += 'Buzz'
    return (msg or x)

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        print(pool.map(FizzBuzz, range(2000000)))
