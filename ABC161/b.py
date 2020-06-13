n, m = map(int, input().split())
a = list(map(int, input().split()))
limit = sum(a) / 4 / m
a.sort()
a = a[::-1]
if a[m-1] < limit:
    print("No")
else:
    print("Yes")