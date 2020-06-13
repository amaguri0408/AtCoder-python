N, K = map(int, input().split())
lst = [False] * (N+1)
for i in range(K):
    d = int(input())
    for j in map(int, input().split()):
        lst[j] = True
ans = -1
# print(lst)
for i in lst:
    if not i:
        ans += 1
print(ans)