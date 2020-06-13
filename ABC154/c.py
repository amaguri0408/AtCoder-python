import time
start = time.time()

n = int(input())
a = list(map(int, input().split()))
# # a = [i for i in range(n)]
# st = set()
# for i in range(n):
#     st.add(a[i])
# if len(st) == n: print("YES")
# else: print("NO")

# print(time.time() - start)

a.sort()
for i in range(n-1):
    if a[i] == a[i+1]:
        print("NO")
        break
else:
    print("YES")