def ladder(x, y, arr):
    dx = [-1, 0, 1]
    dy = [0, -1, 0]
    dir = 1
    while True:
        if dir != 1:
            if 99 < x + dx[dir]:
                if arr[y][x + dx[1]] != 0:
                    dir = 1
                else:
                    dir = 0
            elif x + dx[dir] < 0:
                if arr[y][x + dx[1]] != 0:
                    dir = 1
                else:
                    dir = 2
            nx = x + dx[dir]

        elif dir == 1:
            if x + dx[0] > -1:
                if arr[y][x + dx[0]] != 0:
                    dir = 0
            if x + dx[2] < 100:
                if arr[y][x + dx[2]] != 0:
                    dir = 2
            nx = x + dx[dir]

        if dir != 1:
            if arr[y][nx] == 0:
                dir = 1

        x = x + dx[dir]
        y = y + dy[dir]

        if y == 0:
            return x

for tc in range(1, 11):
    N = int(input())
    arr = []
    arr = [list(map(int, input().split())) for _ in range(100)]
    x = y = 99
    for i in range(len(arr[99])):
        if arr[99][i] == 2:
            x = i
    print(f'#{tc} {ladder(x, y, arr)}')
