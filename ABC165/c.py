N, M, Q = map(int, input().split())
abcd = []
for i in range(Q): abcd.append(list(map(int, input().split())))
ans = 0
per_lst = []
def make_per(lst, n, m):
    n_lst = lst.copy()
    n_lst.append(0)
    if n == 1:
        for i in range(1, m+1):
            n_lst = n_lst.copy()
            n_lst[-1] = i
            if len(n_lst) > 1:
                if i >= n_lst[-2]:
                    per_lst.append(n_lst)
            else:
                per_lst.append(n_lst)
    else:
        for i in range(1, m+1):
            n_lst[-1] = i
            if len(n_lst) > 1:
                if i >= n_lst[-2]:
                    make_per(n_lst, n-1, m)
            else:
                make_per(n_lst, n-1, m)

make_per([], N, M)
# for i in per_lst:
#     print(i)
maxi = 0
for per in per_lst:
    score = 0
    for i in range(Q):
        a, b, c, d = abcd[i][0], abcd[i][1], abcd[i][2], abcd[i][3]
        a -= 1
        b -= 1
        if (per[b] - per[a]) == c: score += d
    if score > maxi: maxi = score
print(maxi)


