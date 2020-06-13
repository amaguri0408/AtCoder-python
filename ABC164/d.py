S = list(input())
rest = [0] * (len(S) + 1)
rest[0] = 0
rd = 1
for i in range(len(S)):
    rest[i+1] = (rest[i] + int(S[-(i+1)]) * rd) % 2019
    rd *= 10
    rd %= 2019
    # print(i, rest[i+1], rest[i], int(S[-(i+2)]), int(S[-(i+2)]) * 10 ** (i+1))
# print(rest)
cnt = [0] * (2019 + 1)
for i in rest: cnt[i] += 1
ans = 0
for i in range(2020):
    ans += cnt[i] * (cnt[i] - 1) // 2
print(ans)