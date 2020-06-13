H1, M1, H2, M2, K = map(int, input().split())
run = (H2 - H1) * 60 + (M2 - M1)
print(run - K)