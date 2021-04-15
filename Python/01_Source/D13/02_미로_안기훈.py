def dfs(r, c, maze):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    global mazes

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if r == N-1 and dr[k] > 0:
            continue
        elif c == N-1 and dc[k] > 0:
            continue
        elif r == 0 and dr[k] < 0:
            continue
        elif c == 0 and dc[k] < 0:
            continue
        if maze[nr][nc] == 0:
            maze[nr][nc] = 1
            dfs(nr, nc, maze)
        elif maze[nr][nc] == 3:
            mazes = 1
            return True


T = int(input())
for tc in range(1, T+1):
    mazes = 0
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                dfs(i, j, maze)
                if mazes:
                    print(f'#{tc} 1')
                else:
                    print(f'#{tc} 0')