T = int(input())
for i in range(T):
    N, A, B, C, D = map(int, input().split())
    dp = [1000000000000000000000000000000] * N**2
    dp[0] = 0
    dp[1] = D
    for j in range(1, N+1):
        dp[j+1] = min(dp[j+1], dp[j] + D)
        dp[j*2] = min(dp[j*2], dp[j] + A)
        dp[j*3] = min(dp[j*3], dp[j] + B)
        dp[j*5] = min(dp[j*5], dp[j] + C)