a, b, c = map(int, input().split())
if a == b or b == c or c == a:
    if a != b or b != c or c != a:
        flug = True
    else:
        flug = False
else:
    flug = False
if flug:
    print("Yes")
else:
    print("No")