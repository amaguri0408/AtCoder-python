N, P = map(int, input().split())
S = input()
ans = 0
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        n = int(S[i:j])
        if n % P == 0:
            ans += 1
print(ans)