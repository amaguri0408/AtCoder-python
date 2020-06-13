N = int(input())
A = list(map(int, input().split()))

up = [0] * (N+1)
down = [0] * (N+1)

up[0] = A[-1]
for i in range(1, N+1):
    up[i] = up[i-1] + A[-(i+1)]

up = up[::-1]
down[0] = 1
for i in range(1, N+1):
    down[i] = (down[i-1] - A[i-1])*2
    if down[i] > up[i]:
        break

flug = True
lst = [0] * (N+1)
for i in range(N+1):
    if flug and down[i] < up[i]:
        lst[i] = down[i]
    else:
        flug = False
        lst[i] = up[i]

# print(up, down, lst)
flug = False
for i in lst:
    if i <= 0:
        flug = True
if flug:
    print(-1)
else:
    print(sum(lst))