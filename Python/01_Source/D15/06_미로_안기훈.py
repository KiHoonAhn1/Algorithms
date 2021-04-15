dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def maze(r, c, arr):
    global result
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr >= 0 and nr < 16 and nc >= 0 and nc < 16:
            if arr[nr][nc] == 0:
                arr[nr][nc] = 1
                maze(nr, nc, arr)
            elif arr[nr][nc] == 3:
                result = 1

for _ in range(1, 11):
    T = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    result = 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                maze(i, j, arr)
                print(f'#{T} {result}')