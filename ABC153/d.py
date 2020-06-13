h = int(input())
mon_num = 1
count = 1
while True:
    if h <= 1:
        break
    else:
        h //= 2
        mon_num *= 2
        count += mon_num
print(count)