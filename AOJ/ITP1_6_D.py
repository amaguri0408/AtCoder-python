n, m = list(map(int, input().split()))
A = []
for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)
b = []
for i in range(m):
    b.append(int(input()))
c = []
for i in range(n):
    kari = 0
    for j in range(m):
        kari += A[i][j] * b[j]
    c.append(kari)
for i in c:
    print(i)