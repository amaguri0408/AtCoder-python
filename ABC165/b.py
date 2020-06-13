X = int(input())
money = 100
ans = 0
if X <= 100:
    print(0)
else:
    while True:
        money = int(money * 1.01)
        ans += 1
        if money >= X:
            print(ans)
            break