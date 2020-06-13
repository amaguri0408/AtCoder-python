N = int(input())

ans = 0

for i in range(2, 10**6+1):
    if N % i != 0: continue
    ans += 1
    cnta = 0
    cntb = 2
    while N % i == 0:
        N //= i
        cnta += 1
        if cnta > cntb:
            cnta -= cntb
            cntb += 1
            ans += 1
    if N == 1:
        break
if N != 1:
    ans += 1


print(ans)