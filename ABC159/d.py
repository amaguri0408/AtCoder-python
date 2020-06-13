n = int(input())
a = list(map(int, input().split()))
# a = [i+1 for i in range(n)]
dct = {}
for i in range(n):
    if a[i] in dct:
        dct[a[i]] += 1
    else:
        dct[a[i]] = 1
tmp3_dct = dct
dct = {}
for key, value in tmp3_dct.items():
    if value > 1:
        dct[key] = value
# print(dct)
tmp_dct = {}
tmp2_dct = {}
for key, value in dct.items():
    tmp_dct[key] = value * (value - 1) // 2
    tmp2_dct[key] = (value - 1) * (value - 2) // 2
# print(tmp_dct, tmp2_dct)
ans_dct = {}
for key, value in dct.items():
    cnt = 0
    for key2, value2 in dct.items():
        if key == key2:
            cnt += tmp2_dct[key2]
        else:
            cnt += tmp_dct[key2]
        # print(key, key2, cnt)
    ans_dct[key] = cnt
# print(ans_dct)
for i in range(n):
    if a[i] in ans_dct:
        print(ans_dct[a[i]])
    else:
        print(0)