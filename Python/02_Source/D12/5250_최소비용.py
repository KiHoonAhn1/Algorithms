dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def route(x, y, fuel):
    global min_fuel
    if fuel >= min_fuel:
        return
    if x == y == N:
        min_fuel = fuel
    if fuel_map[x][y] > fuel:
        fuel_map[x][y] = fuel

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            uphill = 0 if road[nx][ny] - road[x][y] <= 0 else road[nx][ny] - road[x][y]
            route(nx, ny, fuel+1+uphill)
    print(fuel_map)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    fuel_map = [[987654321 for _ in range(N)] for _ in range(N)]
    min_fuel = 987654321
    route(0, 0, 0)
