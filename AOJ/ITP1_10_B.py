import math
a, b, C = map(float, input().split())
C = math.radians(C)
print(1/2 * a * b * math.sin(C))
c = (a ** 2 + b ** 2 - 2 * a * b * math.cos(C)) ** 0.5
print(a + b + c)
print(b * math.sin(C))