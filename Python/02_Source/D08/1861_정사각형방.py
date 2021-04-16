dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def move(x, y, start ,cnt):
    global max_cnt, start_num
    if cnt == 1:
        if max_cnt > N**N - rooms[x][y] + 1:
            return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < N and ny < N:
            if rooms[nx][ny] == rooms[x][y] + 1:
                move(nx, ny, start, cnt+1)

    if cnt > max_cnt:
        max_cnt = cnt
        start_num = start
    elif cnt == max_cnt:
        if start < start_num:
            start_num = start

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [[] for _ in range(N)]
    for i in range(N):
        rooms[i] = list(map(int, input().split()))
    max_cnt = 0
    start_num = 987654321
    for i in range(N):
        for j in range(N):
            move(i, j, rooms[i][j], 1)
    print(f'#{tc}', start_num, max_cnt)