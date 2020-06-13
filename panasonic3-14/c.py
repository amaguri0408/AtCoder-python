a, b, c = map(int, input().split())
# print(a ** 0.5, b ** 0.5, c ** 0.5)
digit = 2000
# right = (c - a - b) * (10 ** digit)
# ab = a * b * (10 ** (digit * 2))
# sqrt_ab = 0
ans = False
def sqrt(n):
    global digit
    n *= (10 ** digit)
    sqrt_n = 0
    for i in range(10 ** 5):
        if i * i * (10 ** (digit * 2)) > n:
            sqrt_n += (i - 1) * (10 ** digit)
            break
    for i in range(1, digit + 1):
        # print(sqrt_ab + 10 * (10 ** (digit - i)) * 2)
        # if sqrt_ab + 10 * (10 ** (digit - i)) * 2 < right:
        #     ans = True
        #     break
        for j in range(1, 10):
            if (sqrt_n + j * (10 ** (digit - i))) ** 2 > n:
                sqrt_n += (j - 1) * (10 ** (digit - i))
                break
            elif j == 9:
                sqrt_n += j * (10 ** (digit - i))
                break
    return sqrt_n
# print(sqrt(a))
if sqrt(a) + sqrt(b) < sqrt(c):
    print("Yes")
else:
    print("No")


# if 2 * sqrt_ab < right or ans:
#     print("Yes")
# else:
#     print("No")

# a, b, c = map(int, input().split())
# if c - a - b > 0 and 4 * a * b < ((c - a - b) ** 2):
#     print("Yes")
# else:
#     print("No")