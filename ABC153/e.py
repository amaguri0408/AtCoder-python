h, n = map(int, input().split())
ab = []
for i in range(n):
    ab.append(list(map(int, input().split())))

###二次元DP
# dp = [[0] * (h + 1) for i in range(n+1)]
# for i in range(n):
#     for j in range(h+1):
#         a = ab[i][0]
#         b = ab[i][1]
#         # print(i, j)
#         if i == 0:
#             if j <= a and j > 0:
#                 dp[i+1][j] = b
#             elif j > a:
#                 dp[i+1][j] = dp[i+1][j-a] + b
#         else:
#             if j <= a:
#                 dp[i+1][j] = min(dp[i][j], b)
#             else:
#                 dp[i+1][j] = min(dp[i][j], dp[i+1][j-a] + b)
# # for i in dp:
# #     print(i)
# print(dp[-1][-1])

###一次元DP
dp = [100000000] * (h+1)
dp[0] = 0
for i in range(1, h+1):
    for j in range(n):
        a = ab[j][0]
        b = ab[j][1]
        # print(i, j)
        temp = i - a
        if temp < 0:
            temp = 0
        need_magic = dp[temp] + b
        if need_magic < dp[i]:
            dp[i] = need_magic
        # dp[i] = min(dp[i], dp[max(i-a, 0)] + b)
        # print(i, j, a, b, dp)
print(dp[-1])

###解説写し
# h, n = map(int, input().split())
# dp = [1000000000] * (h+1)
# dp[0] = 0
# for i in range(n):
#     a, b = map(int, input().split())
#     for j in range(h):
#         # nj = min(j + a, h)
#         if j + a < h: nj = j + a
#         else: nj = h
#         # dp[nj] = min(dp[nj], dp[j] + b)
#         if dp[nj] > dp[j] + b: 
#             dp[nj] = dp[j] + b
# print(dp[h])