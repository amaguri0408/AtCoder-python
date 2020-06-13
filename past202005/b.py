N, M, Q = map(int, input().split())

finish = [[False] * M for _ in range(N)]
score = [N] * M
for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        ans = 0
        for i in range(M):
            if finish[s[1]-1][i]:
                ans += score[i]
        print(ans)
    else: #s[0] == 2
        finish[s[1]-1][s[2]-1] = True
        score[s[2]-1] -= 1
