N, M = map(int, input().split())
A = list(map(int, input().split()))
h = sum(A)
if h > N:
    print(-1)
else:
    print(N-h)