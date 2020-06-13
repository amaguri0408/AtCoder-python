NM = input().split(" ")
N = int(NM[0])
M = int(NM[1])
sc = []
for i in range(M):
    sc.append(input().split(" "))
# print(sc)
for i in range(len(sc)):
    sc[i][0] = int(sc[i][0])-1
    sc[i][1] = int(sc[i][1])
if N == 1: s = 0
else: s = 10**(N-1)
for i in range(s,10**(N)):
    n = []
    for j in str(i):
        n.append(int(j))
    # print(n)
    for k in range(len(sc)):
        # print(sc[k], len(n))
        if len(n) - 1 < int(sc[k][0]):
            break
        # print(n, sc[k], n[int(sc[k][0])], sc[k][1])
        if n[sc[k][0]] != sc[k][1]:
            break
    else:
        print(i)
        break
else:
    print(-1)
