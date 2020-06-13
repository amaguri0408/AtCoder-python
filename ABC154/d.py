import time
start = time.time()

n, k = map(int, input().split())
p = list(map(int, input().split()))
# p = [i for i in range(1, n+1)]
ans = 0
# for i in range(n-k+1):
#     exp = 0
#     for j in range(k):
#         exp += (p[i+j] * (p[i+j] + 1)) / 2 / p[i+j]
#     if exp > ans:
#         ans = exp
total = [0] * n
for i in range(n):
    if i == 0:
        total[i] = p[i]
    else:
        total[i] = total[i-1] + p[i]
maxi_sum = 0
maxi_num = 0
for i in range(k-1, n):
    if i == k-1:
        maxi_sum = total[i]
        maxi_num = i
    else:
        if total[i] - total[i-k] > maxi_sum:
            maxi_sum = total[i] - total[i-k]
            maxi_num = i
# print(maxi_sum, maxi_num)
ans = 0
for i in range(maxi_num - k + 1, maxi_num + 1):
    ans += (p[i] * (p[i] + 1)) / 2 / p[i]
print(ans)

# print(time.time() - start)