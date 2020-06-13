import queue
#queue.Queue()
#que.put(i)
#que.get()

N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)

sign = [-1] * N
que = queue.Queue()
que.put(0)

while not que.empty():
    v = que.get()
    for nv in G[v]:
        if sign[nv] != -1:
            continue
        sign[nv] = v
        que.put(nv)

print("Yes")
for i in sign[1:]:
    print(i+1)