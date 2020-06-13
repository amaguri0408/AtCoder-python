N = int(input())
A = [0] * N
for i in range(N):
    A[i] = list(input())
# for i in A: print(i)
AA = [[] for _ in range(N)]
for y in range(N):
    for x in range(N):
        AA[x].append(A[y][x])
# for i in AA: print(i)
flug = False
ans = ""
for i in range(N):
    if AA[i] == AA[i][::-1]:
        ans = "".join(AA[i])
        flug = True
        break
for i in range(N):
    if A[i] == A[i][::-1]:
        ans = "".join(A[i])
        flug = True
        break
if flug: print(ans)
else: print(-1)