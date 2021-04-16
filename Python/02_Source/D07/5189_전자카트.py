dx = [0, 1]
dy = [1, 0]
def cart(idx, cnt, total):
    global min_battery
    if cnt == N-1:
        min_battery = min(min_battery, total+field[idx][0])
        return
    if min_battery < total:
        return
    for i in range(1, N):
        if visited[i] == 0:
            visited[i] = 1
            cart(i, cnt+1, total+field[idx][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        field[i] = list(map(int, input().split()))
    visited = [0] * N
    min_battery = 987654321
    cart(0, 0, 0)
    print(f'#{tc} {min_battery}')