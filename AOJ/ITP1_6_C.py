n = int(input())
build = [[[0 for i in range(10)]for j in range(3)]for k in range(4)]
for i in range(n):
    b, f, r, v = list(map(int, input().split()))
    build[b-1][f-1][r-1] += v
for b in range(4):
    for f in range(3):
        for r in range(10):
            print("", build[b][f][r], end="")
        print()
    if b != 3: 
        print("####################")