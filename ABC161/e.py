n, k, c = map(int, input().split())
s = input()
enable = []
for i in s:
    if i == 'o':
        enable.append(True)
    else:
        enable.append(False)
work_lst = []
for i in range(n):
    if enable[i]:
        work_lst.append(i)
