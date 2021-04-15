T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    x = y = 0
    maxFlies = 0
    while True:
        flies = 0
        for i in range(y, M+y):
            for j in range(x, M+x):
                flies += arr[i][j]
        if flies > maxFlies:
            maxFlies = flies
        if x == N - M:
            if y == N - M:
                break
            else:
                x = 0
                y += 1
        else:
            x += 1
    print(f'#{tc} {maxFlies}')
