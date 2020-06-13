A, B = map(int, input().split())
a = int(A // 0.08)
ans_lst = []
for i in range(20):
    # print(a, int(a * 0.08) == A)
    if int(a * 0.08) == A:
        ans_lst.append(a)
    a += 1
for i in ans_lst:
    if int(i * 0.1) == B:
        print(i)
        break
else:
    print(-1)