N = int(input())
S = input()
R_lst = []
G_lst = []
B_lst = []
B_exist = [0] * N
for i in range(N):
    if S[i] == 'R':
        R_lst.append(i)
    elif S[i] == 'G':
        G_lst.append(i)
    else: #S[i] == 'B'
        B_lst.append(i)
        B_exist[i] = 1

ans = 0
B_len = len(B_lst)
for r in R_lst:
    for g in G_lst:
        if r < g:
            i, j = r, g
        else:
            i, j = g, r
        ans += B_len

        flug = False
        if j + j - i >= N:
            flug = False
        elif B_exist[j + j - i]:
            flug = True
        if flug:
            ans -= 1
        
        flug = False
        if i - (j - i) < 0:
            flug = False
        elif B_exist[i - (j - i)]:
            flug = True
        if flug:
            ans -= 1
            
        flug = False
        if (i + j) / 2 % 1 != 0:
            flug = False
        elif B_exist[(i + j) // 2]:
            flug = True
        if flug:
            ans -= 1
print(ans)