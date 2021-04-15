def wall(x, y, N, square):
    if x < 0 or x >= N:
        return True
    if y < 0 or y >= N:
        return True
    if square[x][y] != 0:
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    square = [[0] * N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x, y = 0, 0
    dir = 0
    nx, ny = 0, 0

    for i in range(1, N**2+1):
        # 처음 숫자를 넣는다
        square[x][y] = i
        nx = x + dx[dir]
        ny = y + dy[dir]
        if wall(nx, ny, N, square):
            dir = dir + 1
            if dir == 4:
                dir = 0
        x = x + dx[dir]
        y = y + dy[dir]

    print(f'#{tc}')
    for j in range(N):
        for k in range(N):
            print(square[k][j], end=" ")
        print()
