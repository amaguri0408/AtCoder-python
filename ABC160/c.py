k, n = map(int, input().split())
a = list(map(int, input().split()))
max_dif = 0
for i in range(len(a)-1):
    max_dif = max(max_dif, a[i+1] - a[i])
max_dif = max(max_dif, k - a[-1] + a[0])
print(k - max_dif)