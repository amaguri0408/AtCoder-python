n, k = map(int, input().split())
n_k = ""
while True:
    temp = n % k
    if n != 0:
        n_k += str(temp)
    else:
        break
    n //= k
n_k = n_k[::-1]
print(len(n_k))