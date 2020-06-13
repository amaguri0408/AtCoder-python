N = int(input())
a = [[0] * N for _ in range(N)]
for j in range(N):
    for i in range(N):
        a[i][j] = N * (i) + j
# for i in a: print(i)

Q = int(input())
trans = 1
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] in [1, 2] and trans == -1:
        if q[0] == 1: q[0] = 2
        else: q[0] = 1
    elif q[0] == 4 and trans == -1:
        q[1], q[2] = q[2], q[1]
    if q[0] == 1:
        A = q[1]-1
        B = q[2]-1
        a[A], a[B] = a[B], a[A]
    elif q[0] == 2:
        A = q[1]-1
        B = q[2]-1
        for j in range(N):
            a[j][A], a[j][B] = a[j][B], a[j][A]
    elif q[0] == 3:
        trans *= -1
    else:
        A = q[1]-1
        B = q[2]-1
        print(a[A][B])
