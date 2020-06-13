x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p.sort()
q.sort()
r.sort()
red = []
green = []
less = []
for i in range(x):
    red.append(p[-i-1])
for i in range(y):
    green.append(q[-i-1])
# print(red, green)
for i in range(c):
    if len(red) > 0 and len(green) > 0:
        if red[-1] < green[-1]:
            if red[-1] < r[-i-1]:
                del red[-1]
                less.append(r[-i-1])
        else:
            if green[-1] <= r[-i-1]:
                del green[-1]
                less.append(r[-i-1])
    elif len(red) > 0:
        if red[-1] < r[-i-1]:
            del red[-1]
            less.append(r[-i-1])
    elif len(green) > 0:
        if green[-1] <= r[-i-1]:
            del green[-1]
            less.append(r[-i-1])
ans = sum(red) + sum(green) + sum(less)
# print(red, green, less)
print(ans)