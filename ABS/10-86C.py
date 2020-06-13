n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
for i in range(n):
    t, x, y = lst[i][0], lst[i][1], lst[i][2]
    dis = x + y
    t -= dis
    if t >= 0 and t % 2 == 0:
        continue
    else:
        print("No")
        break
else:
    print("Yes")
