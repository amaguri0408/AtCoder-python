a = input().split()
N = int(a[0])
M = int(a[1])
K = int(a[2])
f = []
for i in range(M):
    f.append([int(i) for i in input().split()])
b = []
for i in range(K):
    b.append([int(i) for i in input().split()])

ans = [N-1 for i in range(N)]
for i in range(N):
    for j in range(M):
        if i+1 == f[j][0] or i+1 == f[j][1]:
            ans[i] -= 1
    for j in range(K):
        if i+1 == b[j][0] or i+1 == b[j][1]:
            ans[i] -= 1
for i in ans:
    print(i, end=" ")