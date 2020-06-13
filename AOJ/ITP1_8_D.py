s, p = input(), input()
s += s
for i in range(int(len(s)/2)):
    for j in range(len(p)):
        if s[i + j] != p[j]:
            break
    else:
        print("Yes")
        break
else:
    print("No")