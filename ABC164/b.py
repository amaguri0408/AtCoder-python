A, B, C, D = map(int, input().split())
a = C / B
b = A / D
# print(a, b)
if a % 1 != 0: a = int(a) + 1
if b % 1 != 0: b = int(b) + 1
# print(a, b)
if a > b:
    print("No")
else:
    print("Yes")