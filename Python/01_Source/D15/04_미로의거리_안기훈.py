dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def maze(r, c, arr, visited):
    global result
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr >= 0 and nr < N and nc >= 0 and nc < N:
            if arr[nr][nc] == 0:
                arr[nr][nc] = 1
                visited[nr][nc] = visited[r][c] + 1
                maze(nr, nc, arr, visited)
            elif arr[nr][nc] == 3:
                print(f'#{tc} {visited[r][c]}') # 이건 나오는데
                result = 1
                return 1 # 왜 이게 return이 안되지...


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                maze(i, j, arr, visited)
                if not result:
                    print(f'#{tc} 0')