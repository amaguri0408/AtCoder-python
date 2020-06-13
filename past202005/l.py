N, Q = map(int, input().split())

a = [i+1 for i in range(N)]
for i in range(Q):
    t, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if t == 1:
        a[x], a[x+1] = a[x+1], a[x]
    else:
        if x < 1 and y >= N:
            a = sorted(a)
        elif x < 1:
            a = sorted(a[x:y+1]) + a[y+1:]
        elif y >= N:
            a = a[:x] + sorted(a[x:y+1])
        else:
            a = a[:x] + sorted(a[x:y+1]) + a[y+1:]
    # print(a)
for i in a:
    print(i, end=" ")