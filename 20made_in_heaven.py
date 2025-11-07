import time,math
a = 2
b = 1
while True:
    a *= 2
    b -= 0.000000000001
    time.sleep(b)
    print(a)
