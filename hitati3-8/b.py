A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xyc_lst = []
for i in range(M):
    xyc_lst.append(list(map(int, input().split())))
ans = min(a) + min(b)
for i in range(M):
    x = xyc_lst[i][0]
    y = xyc_lst[i][1]
    c = xyc_lst[i][2]
    price = a[x-1] + b[y-1] - c
    if price < ans:
        ans = price
print(ans)