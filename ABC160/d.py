n, x, y = map(int, input().split())
if x > y: x, y = y, x
ans_lst = [0] * (n)
for i in range(n-1):
    for j in range(i+1, n):
        tmp = j-i
        tmp = min(tmp, abs(i-(x-1)) + abs(j-(y-1)) + 1)
        ans_lst[tmp] += 1
        # print(i, j, tmp)
for i in range(1, len(ans_lst)):
    print(ans_lst[i])