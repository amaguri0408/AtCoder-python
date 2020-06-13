n = []
s = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        n.append(a)
        s.append(list(map(int, input().split())))
for i in range(len(n)):
    m = sum(s[i]) / n[i]
    dis = 0
    for j in range(n[i]):
        dis += (s[i][j] - m) ** 2 / n[i]
    dis = dis ** 0.5
    print(dis)