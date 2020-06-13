lis = []
while True:
    a = [i for i in input().split()]
    if a[1] == "?":
        break
    else:
        lis.append(a)

for i in lis:
    if i[1] == "+":
        print(int(i[0]) + int(i[2]))
    elif i[1] == "-":
        print(int(i[0]) - int(i[2]))
    elif i[1] == "*":
        print(int(i[0]) * int(i[2]))
    elif i[1] == "/":
        print(int(i[0]) // int(i[2]))
