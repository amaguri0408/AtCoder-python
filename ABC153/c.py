n, k = map(int, input().split())
h = list(map(int, input().split()))
# h = [i for i in range(n)]
h = sorted(h)
# print(h[:-1], h)
if k > len(h):
    print(0)
else:
    if k != 0:
        del h[-k:]
    print(sum(h))