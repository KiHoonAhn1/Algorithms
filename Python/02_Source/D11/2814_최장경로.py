def route(idx, cnt):
    global max_cnt
    max_cnt = max(max_cnt, cnt)

    for i in range(1, N+1):
        if adj[idx][i] and visited[i] != 1:
            visited[i] = 1
            route(i, cnt+1)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    max_cnt = 1
    for i in range(M):
        x, y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1

    for i in range(1, N+1):
        visited[i] = 1
        route(i, 1)
        visited[i] = 0

    print(f'#{tc} {max_cnt}')
