N, M = map(int, input().split())
H = list(map(int, input().split()))
AB_lst = [0] * (N+1)
for i in range(N+1): AB_lst[i] = []
for i in range(M):
    A, B = map(int, input().split())
    AB_lst[A].append(B)
    AB_lst[B].append(A)
# print(AB_lst)
ans = 0
for i in range(1, N+1):
    flug = True
    for j in AB_lst[i]:
        if not (H[i-1] > H[j-1]):
            flug = False
    if flug:
        ans += 1
print(ans)
