N, K = map(int, input().split())
head = 0
foot = 0
ans = 0
for i in range(1, N+2):
    head += i-1
    foot += N - (i-1)
    if i >= K:
        ans = (ans + foot - head + 1) % 1000000007
    # print(i, head, foot, ans)
print(ans)