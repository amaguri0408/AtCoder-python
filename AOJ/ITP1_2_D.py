W, H, x, y, r = [int(x) for x in input().split()]
if (0 <= x - r and W >= x + r and 0 <= y - r and H >= y + r):
    print("Yes")
else:
    print("No")