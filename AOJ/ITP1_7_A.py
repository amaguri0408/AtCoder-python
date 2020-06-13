score = []
while True:
    a = list(map(int, input().split()))
    if a[0] == -1 and a[1] == -1 and a[2] == -1:
        break
    else:
        score.append(a)

for i in range(len(score)):
    m, f, r = score[i][0], score[i][1], score[i][2]
    if m == -1 or f == -1:
        print("F")
    elif m + f >= 80:
        print("A")
    elif 65 <= m + f < 80:
        print("B")
    elif 50 <= m + f < 65:
        print("C")
    elif 30 <= m + f < 50:
        if r >= 50:
            print("C")
        else:
            print("D")
    elif m + f < 30:
        print("F") 
