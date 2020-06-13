
def choose2(n):
    return n * (n-1) // 2

n = int(input())
a = list(map(int, input().split()))
dct = {}
for i in range(n):
    if a[i] in dct:
        dct[a[i]] += 1
    else:
        dct[a[i]] = 1
tot = 0
for key, value in dct.items():
    tot += choose2(value)
# print(tot)
for i in range(n):
    ans = tot
    ans -= choose2(dct[a[i]])
    ans += choose2(dct[a[i]]-1)
    print(ans)