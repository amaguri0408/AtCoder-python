import itertools
h, w = map(int, input().split())
map_lst = []
for i in range(h):
    map_lst.append(list(input()))
#0:下 1:右
lst = [i for i in range(h + w - 2)]
lst = list(itertools.combinations(lst,h-1))
ans = 200
for i in lst:
    rc_lst = [1] * (h + w - 2)
    for j in i:
        rc_lst[j] = 0
    bw_lst = []
    if map_lst[0][0] == '.': bw_lst.append(0)
    elif map_lst[0][0] == '#': bw_lst.append(1)
    r = 0
    c = 0
    cnt_b = 0
    # print(rc_lst)
    for j in range(h + w - 2):
        if rc_lst[j] == 0: r += 1
        elif rc_lst[j] == 1: c += 1
        if map_lst[r][c] == ".":
            if bw_lst[-1] == 1:
                cnt_b += 1
            bw_lst.append(0)
        elif map_lst[r][c] == "#":
            bw_lst.append(1)
    if map_lst[h-1][w-1] == '#': cnt_b += 1
    ans = min(ans, cnt_b)
    # print(rc_lst, bw_lst, cnt_b)
print(ans)