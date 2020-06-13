import itertools
h, w = map(int, input().split())
map_lst = []
for i in range(h):
    map_lst.append(list(input()))
dp = [[200] * (w) for i in range(h)]
if map_lst[0][0] == '.': dp[0][0] = 0
else: dp[0][0] = 1
# for i in dp:
#     print(i)
for c in range(w):
    for r in range(h):
        over = 0
        left = 0
        if r > 0:
            if map_lst[r-1][c] == '.' and map_lst[r][c] == '#':
                over = 1
        if c > 0:
            if map_lst[r][c-1] == '.' and map_lst[r][c] == '#':
                left = 1
        if r == 0 and c == 0:
            continue
        elif r == 0:
            dp[r][c] = dp[r][c-1] + left
        elif c == 0:
            dp[r][c] = dp[r-1][c] + over
        else:
            dp[r][c] = min(dp[r-1][c] + over, dp[r][c-1] + left)
# for i in dp:
#     print(i)
print(dp[-1][-1])