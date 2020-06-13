lst = []
while True:
    a = list(map(int, input().split()))
    if a[0] == 0 and a[1] == 0:
        break
    else:
        lst.append(a)
for i in range(len(lst)):
    for y in range(lst[i][0]):
        for x in range(lst[i][1]):
            print("#", end="")
        print()
    print()