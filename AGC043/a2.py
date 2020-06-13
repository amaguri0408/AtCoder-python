import itertools
h, w = map(int, input().split())
map_lst = []
for i in range(h):
    map_lst.append(list(input()))
b_lst = [[-1] * w for i in range(h)]
b_lst[0][0] = 0
e_lst = [[0, 0]]
#be_r, be_c:調べる前の座標, r, c:調べる座標
def main(be_r, be_c, r, c, bw, cnt):
    # print(r, c)
    if b_lst[r][c] != -1:
        return
    if map_lst[be_r][be_c] == map_lst[r][c]:
        b_lst[r][c] = cnt
        if c < w-1: main(r, c, r, c+1, map_lst[r][c], cnt)
        if r < h-1: main(r, c, r+1, c, map_lst[r][c], cnt)
    else:
        b_lst[r][c] = cnt + 1
        e_lst.append([r, c])

cnt_b = 0
while True:
    tmp_lst = e_lst
    if tmp_lst == []:
        break
    e_lst = []
    # print(tmp_lst, b_lst)
    for i in tmp_lst:
        r, c = i[0], i[1]
        if c < w-1: main(r, c, r, c+1, map_lst[r][c], cnt_b)
        if r < h-1: main(r, c, r+1, c, map_lst[r][c], cnt_b)
    cnt_b += 1
for i in b_lst:
    print(i)
if map_lst[0][0] == '.':
    print(b_lst[-1][-1]//2)
else:
    print(b_lst[-1][-1]+1//2)