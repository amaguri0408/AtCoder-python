N, M, Q = map(int, input().split())

G = [[] for _ in range(N)]
for i in range(M):
    uv = list(map(int, input().split()))
    for i, value in enumerate(uv):
        uv[i] = value - 1
    G[uv[0]].append(uv[1])
    G[uv[1]].append(uv[0])

c = list(map(int, input().split()))
for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        print(c[s[1]-1])
        for i in G[s[1]-1]:
            c[i] = c[s[1]-1]
    else: #s[0] == 2
        print(c[s[1]-1])
        c[s[1]-1] = s[2]