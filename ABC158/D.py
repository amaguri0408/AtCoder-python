S = input()
Q = int(input())
reverse = 1
head = ""
tail = ""
for i in range(Q):
    a = input().split()
    if a[0] == "1":
        reverse *= -1
    elif a[1] == "1":
        if reverse == 1:
            head += a[2]
        else:
            tail += a[2]
    else:
        if reverse == 1:
            tail += a[2]
        else:
            head += a[2]
# for i in range(Q):
#     a = input().split()
#     if a[0] == "1":
#         reverse *= -1
#     elif a[1] == "1":
#         if reverse == 1:
#             S = a[2] + S
#         else:
#             S = S + a[2]
#     else:
#         if reverse == 1:
#             S = S + a[2]
#         else:
#             S = a[2] + S
S = head[::-1] + S + tail
if reverse == -1:
    S = S[::-1]
print(S)