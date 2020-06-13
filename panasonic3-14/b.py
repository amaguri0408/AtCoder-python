h, w = map(int, input().split())
ans = 0
ans += (h // 2) * (w // 2) * 2
if h % 2 != 0:
    ans += w // 2
if w % 2 != 0:
    ans += h // 2
if h % 2 != 0 and w % 2 != 0:
    ans += 1
if h == 1 or w == 1:
    ans = 1
print(ans)