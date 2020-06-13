W = input()
T = []
while True:
    a = input().split()
    if a == ["END_OF_TEXT"]:
        break
    else:
        for i in a:
            T.append(i)
cnt = 0
for i in range(len(T)):
    if str.lower(T[i]) == W:
        cnt += 1
print(cnt)