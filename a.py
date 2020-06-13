h, a = map(int, input().split())
cnt = 0
while True:
    cnt += 1
    h -= a
    if h <= 0:
        break
print(cnt)