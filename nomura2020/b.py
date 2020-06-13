S = input()

ns = ""
for i in S:
    if i == '?':
        ns += 'D'
    else:
        ns += i

print(ns)