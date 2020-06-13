n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for p in range(1, 4):
    D = 0
    for i in range(n):
        D += abs(x[i] - y[i]) ** p
    D = D ** (1/p)
    print(D)
D = 0
for i in range(n):
    tmp = abs(x[i] - y[i])
    if D < tmp:
        D = tmp
print(D)