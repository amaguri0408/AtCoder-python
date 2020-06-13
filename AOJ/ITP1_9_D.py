s = input()
s_lst = []
# for i in s:
#     s_lst.append(i)
s_lst = list(s)
print(s_lst)
q = int(input())
order = [0] * q
for i in range(q):
    order[i] = input().split()
    order[i][1] = int(order[i][1])
    order[i][2] = int(order[i][2])
for i in range(q):
    if order[i][0] == "print":
        s = "".join(s_lst)
        # print(order[i], s_lst )
        print(s[order[i][1]:order[i][2]+1])
    elif order[i][0] == "reverse":
        for j in range((order[i][2]-order[i][1]+1)//2):
            s_lst[order[i][1]+j], s_lst[order[i][2]-j] = s_lst[order[i][2]-j], s_lst[order[i][1]+j]
        # print(order[i], s_lst )
    elif order[i][0] == "replace":
        for j in range(len(order[i][3])):
            s_lst[order[i][1] + j] = order[i][3][j]
        # print(order[i], s_lst )