import sys
s = sys.stdin.read()
# s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
cnt = [0] * len(alpha)
for i in s:
    for j in range(len(alpha)):
        if str.lower(i) == alpha[j]:
            cnt[j] += 1
for i in range(len(alpha)):
    print(alpha[i], ":", cnt[i])