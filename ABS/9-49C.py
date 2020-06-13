s = input()
while True:
    if s == "":
        print("YES")
        break
    if s[len(s)-7:] == "dreamer":
        s = s[:len(s)-7]
    elif s[len(s)-6:] == "eraser":
        s = s[:len(s)-6]
    elif s[len(s)-5:] == "dream" or s[len(s)-5:] == "erase":
        s = s[:len(s)-5]
    else:
        print("NO")
        break