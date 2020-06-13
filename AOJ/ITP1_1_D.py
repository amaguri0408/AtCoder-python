S = int(input())
h = S // (60 * 60)
s = S % (60 * 60)
m = s // 60
s = s % 60
print("{}:{}:{}".format(h, m, s))