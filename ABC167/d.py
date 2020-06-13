N, K = map(int, input().split())
A = list(map(int, input().split()))
tele = [0] * N
for i in range(N):
    tele[i] = A[i] - 1
now = 0
cnt = 0
exp = [False] * N
period = 0
loop = False
start = -1
while cnt < K:
    exp[now] = True
    now = tele[now]
    cnt += 1
    if loop:
        period += 1
        if now == start:
            loop = False
            cnt = K - ((K - cnt) % period)
    if exp[now] and (not loop):
        loop = True
        start = now
    # print(now, exp, cnt, period, start)
print(now+1)