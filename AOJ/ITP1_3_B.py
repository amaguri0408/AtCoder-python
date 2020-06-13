lis = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        lis.append(a)

for i in range(len(lis)):
    print("Case {}: {}".format(i+1, lis[i]))