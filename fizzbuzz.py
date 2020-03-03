def FizzBuzz(x):
    msg = ''
    if x % 3 == 0: msg += 'Fizz'
    if x % 5 == 0: msg += 'Buzz'
    return (msg or x)

for i in range(0,101): print(i, " : ", FizzBuzz(i))
