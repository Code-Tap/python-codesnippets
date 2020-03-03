import time

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                print(f"{i} {j} {k} {l}", end="\r")
                time.sleep(.001)