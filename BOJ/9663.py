dx = [1, 1, -1, -1]
dy = [1, -1, -1, 1]

def chess(y, arr, cnt):
    global result
    c_arr = arr[:]
    if y >= N:
        return
    if cnt >= N-1:
        result += 1
    for i in range(N):
        if arr[y][i] == 0:
            print(arr)
            print(y, i)
            for j in range(N):
                c_arr[y][j] = 1
                c_arr[j][i] = 1
            for k in range(4):
                nx = i + dx[k]
                ny = y + dy[k]
                a = 0
                while nx >= 0 and nx < N and ny >= 0 and ny < N:
                    c_arr[nx][ny] = 1
                    a += 1
                    nx = i + dx[k] * a
                    ny = y + dy[k] * a
            print(y, cnt)
            chess(y+1, c_arr, cnt+1)

N = int(input())
result = 0
for i in range(N):
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for j in range(N):
        arr[0][j] = 1
        arr[j][i] = 1
    for k in range(0, 4):
        if k == 1 or k == 2:
            continue
        nx = i + dx[k]
        ny = dy[k]
        a = 1
        while nx >= 0 and nx < N and ny >= 0 and ny < N:
            arr[nx][ny] = 1
            a += 1
            nx = i + dx[k] * a
            ny = dy[k] * a
    chess(1, arr, 1)
print(result)