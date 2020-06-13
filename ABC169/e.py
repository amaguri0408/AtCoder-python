N = int(input())
A = []
B = []
for i in range(N):
    AB = list(map(int, input().split()))
    A.append(AB[0])
    B.append(AB[1])
A = sorted(A)
B = sorted(B)

if N % 2 == 0:
    min1 = A[N//2-1]
    min2 = A[N//2]
    max2 = B[-N//2]
    max1 = B[-N//2-1]
    # print(min1, min2, max1, max2)
    ans = ((max2 + max1) / 2 - (min2 + min1) / 2) * 2 + 1
else:
    mini = A[N//2]
    maxi = B[-N//2]
    # print(mini, maxi)
    ans = maxi - mini + 1
print(int(ans))