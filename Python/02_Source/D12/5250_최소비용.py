dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def route(x, y):
    queue = [(x, y)]
    while queue:
        temp = queue.pop(0)
        for i in range(4):
            nx = temp[0] + dx[i]
            ny = temp[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                uphill = 0 if road[nx][ny] - road[temp[0]][temp[1]] <= 0 else road[nx][ny] - road[temp[0]][temp[1]]
                if fuel_map[nx][ny] > fuel_map[temp[0]][temp[1]] + 1 + uphill:
                    fuel_map[nx][ny] = fuel_map[temp[0]][temp[1]] + 1 + uphill
                    queue.append([nx, ny])
    return fuel_map[N-1][N-1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    fuel_map = [[987654321 for _ in range(N)] for _ in range(N)]
    fuel_map[0][0] = 0
    print(f'#{tc} {route(0, 0)}')