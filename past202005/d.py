N = int(input())
s = [0] * 5
for i in range(5):
    s[i] = input()
s2 = [0] * (4*N + 1)
for i in range(4 * N + 1):
    tmp = ""
    for j in range(5):
        if s[j][i] == '.':
            tmp += '0'
        else:
            tmp += '1'
    s2[i] = tmp
# for i in s2:
#     print(i)
num = [["11111", "10001", "11111"],     #0
        ["01001", "11111", "00001"],    #1
        ["10111", "10101", "11101"],    #2
        ["10101", "10101", "11111"],    #3
        ["11100", "00100", "11111"],    #4
        ["11101", "10101", "10111"],    #5
        ["11111", "10101", "10111"],    #6
        ["10000", "10000", "11111"],    #7
        ["11111", "10101", "11111"],    #8
        ["11101", "10101", "11111"]]    #9

for i in range(N):
    for j in range(10):
        flug = True
        for k in range(3):
            if s2[i*4+k+1] != num[j][k]:
                flug = False
        if flug:
            print(j, end = "")
            break
    # if s2[i*4+1] == num1[0] and s2[i*4+2] == num1[1] and s2[i*4+3] == num1[2]:
    #     print(0)