T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0 for _ in range(21)] for _ in range(N)]
    arr[0][10] = 1
    for i in range(1, N):
        for j in range(1, 20):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]

    print(f'#{tc}')
    for i in range(N):
        for j in range(21):
            if arr[i][j] != 0:
                print(arr[i][j], end=' ')
        print()