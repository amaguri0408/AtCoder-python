h, w, k = map(int, input().split())
s = []
for i in range(h):
    s.append(list(map(int, list(input()))))
mini = 1010
for i in range(1<<(h-1)):
# for i in [0]:
    bit = (i<<1) | (1<<h) | (1)
    # print(bin(bit))
    h_cut = []
    for j in range(h+1):
        if (bit>>j) & 1 == 1:
            h_cut.append(j)
    l_cut = [0, 1]
    j = 0
    while True:
        flug = True
        left = l_cut[j]
        right = l_cut[j+1]
        for l in range(len(h_cut)-1):
            high = h_cut[l+1]
            low = h_cut[l]
            cnt = 0
            for x in range(left, right):
                for y in range(low, high):
                    if s[y][x] == 1:
                        cnt += 1
            if cnt > k:
                flug = False
                break
        if flug:
            if right >= w:
                break
            else:
                l_cut[j+1] += 1
        else:
            # if right >= w:
            #     break
            l_cut.append(l_cut[j+1])
            l_cut[j+1] -= 1
            j += 1
        # print(h_cut, j, left, right, flug, l_cut)
    cnt_cut = len(h_cut) + len(l_cut) - 4
    mini = min(mini, cnt_cut)
print(mini)