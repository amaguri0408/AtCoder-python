A, B = input().split()
A = int(A)
# B = int(float(B) * 100)
B = B.split(".")
B = int(B[0]) * 100 + int(B[1])
# print(B)
print(A * B // 100)