T = int(input())
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def square(r, c, cnt):
    global maxCnt, num
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[r][c] + 1 == arr[nr][nc]:
            cnt += 1
            square(nr, nc, cnt)
            if maxCnt < cnt:
                maxCnt = cnt
                num = arr[r][c] - cnt + 2
            elif maxCnt == cnt:
                if num > arr[r][c] - cnt + 2:
                    num = arr[r][c] - cnt + 2
        else:
            continue

for tc in range(1, T+1):
    maxCnt = 0
    num = 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            square(i, j, 1)
    print(f'#{tc} {num} {maxCnt}')
