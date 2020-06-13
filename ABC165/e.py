N, M = map(int, input().split())
lst = []
if N % 2 == 1:
    for i in range(1, N//2 + 1):
        lst.append([i, N-i])
else:
    for i in range(1, N//2 + 1):
        if i <= (N // 4):
            lst.append([i, N-i])
        else:
            lst.append([i, N-(i+1)])

for i in range(M):
    for j in lst[i]:
        print(j, end=" ")
    print()