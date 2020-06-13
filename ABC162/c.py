import math

def gcd(a, b, c):
    tmp = math.gcd(a, b)
    tmp = math.gcd(tmp, c)
    return tmp

K = int(input())
K += 1
ans = 0
for i in range(1, K):
    for j in range(i, K):
        for k in range(j, K):
            if i == j == k:
                ans += gcd(i, j, k) 
            elif i == j or j == k or k == i:
                ans += gcd(i, j, k) * 3
            else:  # i != j != k
                ans += gcd(i, j, k) * 6
print(ans)