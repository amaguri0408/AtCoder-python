X = int(input())
a = 1
flug = True
while flug:
    b = -119
    while b <= 118:
        if a ** 5 - b ** 5 == X:
            print(a, b)
            flug = False
            break
        else:
            b += 1
    a += 1
