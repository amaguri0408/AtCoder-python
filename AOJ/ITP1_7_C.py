r, c = map(int, input().split())
table = [[0 for i in range(c+1)]for j in range(r+1)]
for i in range(r):
    a = list(map(int, input().split()))
    for j in range(c):
        table[i][j] = a[j]
for i in range(r):
    for j in range(c):
        table[i][-1] += table[i][j]
        table[-1][j] += table[i][j]
    table[-1][-1] += table[i][-1]
for i in range(r+1):
    for j in range(c+1):
        if j > 0:
            print(" ", end="")
        print(table[i][j], end="")
    print()
