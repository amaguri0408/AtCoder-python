N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
    a = list(map(int, input().split()))
    C.append(a[0])
    A.append(a[1:])

mini = 12 * 100000 + 1
for bit in range(1<<N):
    A_sum = [0] * M
    price = 0
    for i in range(N):
        if (bit >> i) & 1:
            price += C[i]
            for j in range(M):
                A_sum[j] += A[i][j]
    flug = True
    for i in A_sum:
        if i < X:
            flug = False
            break
    if flug:
        mini = min(mini, price)
if mini == 12 * 100000 + 1: print(-1)
else: print(mini)