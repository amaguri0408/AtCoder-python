n, a, b = map(int, input().split())
lst = []
for i in range(n+1):
    kari = 0
    for j in str(i):
        kari += int(j)
    if a <= kari <= b:
        lst.append(i)
print(sum(lst))