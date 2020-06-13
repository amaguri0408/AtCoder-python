N = int(input())
A = list(map(int, input().split()))
able_up = [0] * N
able_down = [0] * N
for i in range(N):
    if (i-A[i]) >= 0: able_up[i-A[i]] += 1
    if (i+A[i]) < N: able_down[i+A[i]] += 1
# print(able_up)
# print(able_down)
ans = 0
for i in range(N):
    ans += able_up[i] * able_down[i]
print(ans)