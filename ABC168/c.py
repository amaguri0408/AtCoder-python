import math
A, B, H, M = map(int, input().split())

day_min = 12 * 60
now_min = H * 60 + M
# print(day_min, now_min)
a_ang = now_min * 360 / day_min
b_ang = M * 6
# print(a_ang, b_ang)
tri_ang = min(abs(a_ang - b_ang), abs(a_ang - b_ang + 360), abs(a_ang - b_ang - 360))
# print(tri_ang)
# print(math.cos(tri_ang * 2 * math.pi / 360))
ans = A**2 + B**2 - 2 * A * B * math.cos(tri_ang * math.pi / 180)
print(ans ** 0.5)