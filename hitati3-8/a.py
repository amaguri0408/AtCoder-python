S = input()
for i in range(1, 6):
    if "hi" * i == S:
        print("Yes")
        break
else:
    print("No")