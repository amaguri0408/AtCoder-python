lis = []
while True:
    xy = [int(i) for i in input().split()]
    if xy[0] == 0 and xy[1] == 0:
        break
    else:
        lis.append(xy)

for i in lis:
    if i[0] > i[1]:
        print(i[1], i[0])
    else:
        print(i[0], i[1])