n, y = map(int, input().split())
for i in range(n+1):
    for j in range(i, n+1):
        num1 = i
        num2 = j - i
        num3 = n - j
        # print(num1, num2, num3)
        if num1 * 1000 + num2 * 5000 + num3 * 10000 == y:
            print(num3, num2, num1)
            break
    else:
        continue
    break
else:
    print(-1, -1, -1)