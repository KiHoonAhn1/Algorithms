T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = ['0' for _ in range(N)]
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        L, R = L-1, R-1
        for j in range(L, R+1):
            arr[j] = str(i)
    print(f'#{tc} {" ".join(arr)}')