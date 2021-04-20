dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

def chess(idx, visited):
    global result
    if idx == N:
        result += 1
        return

    for y in range(N):
        copy_visited = [[0 for _ in range(N)] for _ in range(N)]
        for a in range(N):
            for b in range(N):
                copy_visited[a][b] = visited[a][b]
        if copy_visited[idx][y] == 0:
            copy_visited[idx][y] = 1
            for i in range(8):
                nx = idx + dx[i]
                ny = y + dy[i]
                while nx >= 0 and ny >= 0 and nx < N and ny < N:
                    copy_visited[nx][ny] = 1
                    nx += dx[i]
                    ny += dy[i]
            chess(idx+1, copy_visited)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    result = 0
    chess(0, visited)
    print(f'#{tc} {result}')