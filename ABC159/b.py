s = input()
n = len(s)
s2 = s[:(n-1)//2]
s3 = s[(n+3)//2-1:]
flug = True
for i in range(len(s)//2):
    end = -i - 1
    if s[i] != s[end]:
        flug = False
        break
for i in range(len(s2)//2):
    end = -i - 1
    if s2[i] != s2[end]:
        flug = False
        break
for i in range(len(s3)//2):
    end = -i - 1
    if s3[i] != s3[end]:
        flug = False
        break
if flug: print("Yes")
else: print("No")