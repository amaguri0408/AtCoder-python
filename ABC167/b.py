A, B, C, K = map(int, input().split())
ans = 0
if K < A:
    ans = K
else:
    ans += A
    K -= A
    K -= B
    if K > 0:
        ans -= K
print(ans)