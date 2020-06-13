N, A, B = map(int, input().split())
ans = 0
ans = (N // (A+B)) * A
kari = N % (A+B)
if kari > A:
    ans += A
else:
    ans += kari
print(ans)