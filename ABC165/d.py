A, B, N = map(int, input().split())
# for x in range(N+1+20):
#     a = int(A * x / B) - A * int(x / B)
#     print(a)
if N < B-1:
    x = N
else:
    x = B - 1
print(int(A * x / B) - A * int(x / B))