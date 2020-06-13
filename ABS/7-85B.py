n = int(input())
d = []
for i in range(n):
    a = int(input())
    if not a in d:
        d.append(a)
print(len(d))
