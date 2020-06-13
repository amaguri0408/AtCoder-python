n = int(input())
cards = []
tarou = 0
hanako = 0
for i in range(n):
    a, b = input().split()
    if a < b:
        hanako += 3
    elif a > b:
        tarou += 3
    else:
        hanako += 1
        tarou += 1
print(tarou, hanako)