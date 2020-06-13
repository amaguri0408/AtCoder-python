lst = []
while True:
    a = input()
    if a == "0":
        break
    else:
        lst.append(a)
for i in lst:
    ans = 0
    for j in i:
        ans += int(j)
    print(ans)