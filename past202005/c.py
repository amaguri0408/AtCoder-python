# A, R, N = map(int, input().split())
# # ans = A * R ** (N-1)
# # if ans > 10 ** 9:
# #     print("large")
# # else:
# #     print(ans)

# ans = 1
# n = N - 1
# x = R
# while n > 0:
#     if (n|1) == 1:
#         ans *= x
#     x *= x
#     n //= 2
#     # print(ans, n, x)
# ans *= A
# if ans > 10 ** 9:
#     print("large")
# else:
#     print(ans)



def pow_k(x, n):
    if n == 0:
        return 1
    K = 1
    while n > 1:
        if x > 1000000000:
            return 10000000000
        if n % 2 != 0:
            K *= x
        x *= x
        n //= 2
    return K * x

A, R, N = map(int, input().split())

ans = pow_k(R, N-1) * A
if ans > 10 ** 9:
    print("large")
else:
    print(ans)
