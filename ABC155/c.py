# n = int(input())
# s = []
# s_cnt = [0] * n
# for i in range(n):
#     temp = input()
#     if not temp in s:
#         s.append(temp)
#     s_cnt[s.index(temp)] += 1
# maxi = max(s_cnt)
# ans_lst = []
# for i in range(len(s)):
#     if s_cnt[i] == maxi:
#         ans_lst.append(s[i])
# ans_lst.sort()
# ans = ""
# for i in range(len(ans_lst)):
#     ans += ans_lst[i]
#     if i != len(ans_lst) - 1:
#         ans += "\n"
# print(ans)

n = int(input())
s_dict = dict()
for i in range(n):
    a = input()
    if a in s_dict:
        s_dict[a] += 1
    else:
        s_dict.update({a : 1})
maxi = max(s_dict.values())
ans_lst = []
for key, value in s_dict.items():
    if value == maxi:
        ans_lst.append(key)
ans_lst.sort()
for i in ans_lst:
    print(i)
# print(maxi)
# for key, value in s_dict.items():
#     if value == maxi:
#         print(key)