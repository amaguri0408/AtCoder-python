import time

N, M = map(int, input().split())
a = list(map(int, input().split()))

ate_lst = [0] * N
for i in range(M):
    left = 0
    right = len(ate_lst)-1
    while True:
        length = (right - left) // 2
        mid = left + length
        # print(left, right, length, mid, ate_lst)
        #終了
        if length < 1:
            if a[i] > ate_lst[mid]:
                ate_lst[mid] = a[i]
                print(mid+1)
            else:
                if right == len(ate_lst)-1:
                    if a[i] > ate_lst[right]:
                        ate_lst[mid+1] = a[i]
                        print(mid+1+1)
                    else:
                        print(-1)
                else:
                    ate_lst[mid+1] = a[i]
                    print(mid+1+1)
            break
        #次回探索
        if a[i] > ate_lst[mid]:
            right = mid
        else:
            left = mid + 1
        # time.sleep(1)