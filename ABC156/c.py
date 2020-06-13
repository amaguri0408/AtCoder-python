n = int(input())
x_lst = list(map(int, input().split()))
mini = 1000000
for x in range(1, 101):
    power = 0
    for i in range(n):
        power += (x_lst[i] - x) ** 2
    if power < mini:
        mini = power
print(mini)