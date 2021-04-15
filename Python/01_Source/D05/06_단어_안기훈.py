T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N-1):
            if arr[i][j] == 1:
                cnt += 1
            elif arr[i][j] == 0:
                cnt = 0
            if cnt == K and arr[i][j+1] == 0:
                result += 1
        if arr[i][N-1] == 1:
            cnt += 1
            if cnt == K:
                result += 1

    # 세로
    for i in range(N):
        cnt = 0
        for j in range(N-1):
            if arr[j][i] == 1:
                cnt += 1
                if cnt == K and arr[j+1][i] == 0:
                    result += 1
            elif arr[j][i] == 0:
                cnt = 0
        if arr[N-1][i] == 1:
            cnt += 1
            if cnt == K:
                result += 1
    print(f'#{tc} {result}')