a, b, c = map(int, input().split())
con = 0
for i in range(a, b+1):
    if c % i == 0:
        con += 1
print(con)