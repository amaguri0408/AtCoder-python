lst = []
while True:
    a = list(map(int, input().split()))
    if a[0] == a[1] == 0:
        break
    else:
        lst.append(a)
for nx in lst:
    con = 0
    for i in range(1, nx[0]-1):
        for j in range(i+1, nx[0]):
            for k in range(j+1, nx[0]+1):
                if i + j + k == nx[1]:
                    con += 1
    print(con)