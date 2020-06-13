a1, a2, a3 = input(), input(), input()
a1 = [int(i) for i in a1.split()]
a2 = [int(i) for i in a2.split()]
a3 = [int(i) for i in a3.split()]
A = [a1, a2, a3]
N = int(input())
b = []
for i in range(N):
    b.append(int(input()))
for i in range(len(b)):
    for j in range(len(A)):
        for k in range(len(A[0])):
            if b[i] == A[j][k]:
                A[j][k] = 0
ans = 0
for i in range(3):
    if A[0][i] == 0 and A[1][i] == 0 and A[2][i] == 0:
        ans = 1
    if A[i][0] == 0 and A[i][1] == 0 and A[i][2] == 0:
        ans = 1
if A[0][0] == 0 and A[1][1] == 0 and A[2][2] == 0:
    ans = 1
if A[2][0] == 0 and A[1][1] == 0 and A[0][2] == 0:
    ans = 1
if ans == 1:
    print("Yes")
else:
    print("No")