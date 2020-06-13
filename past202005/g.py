import queue
import time

N, X, Y = map(int, input().split())
max_xy = 201
block = [[False] * (max_xy * 2 + 1) for _ in range((max_xy * 2 + 1) )]
for i in range(N):
    x, y = map(int, input().split())
    block[y+max_xy][x+max_xy] = True

dist = [[-1] * (max_xy * 2 + 1) for _ in range((max_xy * 2 + 1) )]
dist[0+max_xy][0+max_xy] = 0
que = queue.Queue()
que.put([0+max_xy,0+max_xy])

def get_dir(pos):
    lst = []
    x = pos[0]
    y = pos[1]
    lst.append([x+1, y+1])
    lst.append([x, y+1])
    lst.append([x-1, y+1])
    lst.append([x+1, y])
    lst.append([x-1, y])
    lst.append([x, y-1])
    return lst

while not que.empty():
    v = que.get()
    for nv in get_dir(v):
        # print(nv)
        if (nv[0] > 402 
                or nv[1] > 402
                or nv[0] < 0
                or nv[1] < 0):
            continue
        if dist[nv[1]][nv[0]] != -1:
            continue
        if block[nv[1]][nv[0]]:
            continue
        # print("OK")
        dist[nv[1]][nv[0]] = dist[v[1]][v[0]] + 1
        que.put(nv)
    if dist[Y+max_xy][X+max_xy] != -1:
        print(dist[Y+max_xy][X+max_xy])
        break
    # print(v, get_dir(v))
    # for i in dist[0+max_xy:3+max_xy]:
    #     print(i[0+max_xy:3+max_xy])
    # time.sleep(1)
else:
    print(-1)

# for i in dist[-5+max_xy:5+max_xy]:
#     print(i[-5+max_xy:5+max_xy])