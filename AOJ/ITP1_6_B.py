n = int(input())
lst = []
for i in range(n):
    a = input().split()
    a[1] = int(a[1])
    lst.append(a)
for i in ["S", "H", "C", "D"]:
    for j in range(1, 14):
        if [i, j] in lst:
            continue
        else:
            print(i, j)