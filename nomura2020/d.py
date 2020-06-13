N = int(input())
P = list(map(int, input().split()))
NUM = 10**9 + 7

for i in range(len(P)):
    P[i] -= 1

#基本的な道の数
#既知→未知の道の数
base = N
cnt = 0
k_unk_num = 0
for i, value in enumerate(P):
    if value >= 0:
        if P[value] == i:
            cnt += 1
        elif P[value] == -2:
            k_unk_num += 1
base -= cnt // 2

#未知の道の数
unknown_num = 0
for i in P:
    if i < 0:
        unknown_num += 1

# print(base, unknown_num, k_unk_num)

ans = 0
ans = (ans + base * (N-1) ** unknown_num) % NUM
# print(ans)
ans = int(ans - k_unk_num * (N-1) ** (unknown_num-1) + NUM) % NUM
# print(ans)
if unknown_num > 1:
    ans = (ans - (unknown_num * (unknown_num-1) // 2) * (N-1) ** (unknown_num-2) + NUM) % NUM

print(ans)