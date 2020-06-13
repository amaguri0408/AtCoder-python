cards = []
i = 0
while True:
    a = input()
    if a == "-":
        break
    cards.append(a)
    m = int(input())
    h = []
    for j in range(m):
        h.append(int(input()))
    for j in h:
        cards[i] = cards[i][j:] + cards[i][:j]
    i += 1
for i in cards:
    print(i)