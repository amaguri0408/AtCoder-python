N, L = map(int, input().split())
X = list(map(int, input().split()))
x = [False] * (L+1)
for i in X:
    x[i] = True
T1, T2, T3 = map(int, input().split())

dp = [100000000000] * (L+1)
dp[0] = 0
for i in range(1, L+1):
    if x[i]: exist_T3 = T3
    else: exist_T3 = 0
    dp[i] = min(dp[i], dp[i-1] + T1 + exist_T3)
    if i >= 2:
        dp[i] = min(dp[i], dp[i-2] + T1 + T2 + exist_T3)
    if i >= 4:
        dp[i] = min(dp[i], dp[i-4] + T1 + 3 * T2 + exist_T3)
    if i == L:
        dp[i] = min(dp[i], dp[i-3] + T1//2 + T2//2*5)
        dp[i] = min(dp[i], dp[i-2] + T1//2 + T2//2*3)
        dp[i] = min(dp[i], dp[i-1] + T1//2 + T2//2)
print(dp[-1])
# print(dp)