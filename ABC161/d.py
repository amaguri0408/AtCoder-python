import sys
K = int(input())
if K < 10:
    print(K)
    sys.exit()
lst = [[str(i)] for i in range(10)]
i = 9
while True:
    new_lst = [[] for j in range(10)]
    for j in range(10):     #0-9までについて
        for k in range(-1, 2):  #-1, 0, +1の3つについて
            if j == 0 and k == -1:
                continue
            if j == 9 and k == 1:
                break
            for l in lst[j+k]:
                tmp = str(j) + str(l)
                new_lst[j].append(tmp)
                # print(i, K , i == K)
                if j != 0:
                    i += 1
                    if i == K:
                        print(int(tmp))
                        sys.exit()
    # print(i, new_lst)
    lst = new_lst.copy()