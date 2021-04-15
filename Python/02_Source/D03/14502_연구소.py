dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
max_result = 0

def virus():
    global max_result
    copy_lab = [[0 for _ in range(N)] for _ in range(M)]
    for i in range(M):
        for j in range(N):
            copy_lab[i][j] = lab[i][j]
    result = 0
    arr = []
    for i in range(M):
        for j in range(N):
            if copy_lab[i][j] == 2:
                arr.append([i,j])
    while arr:
        x, y = arr[-1][0], arr[-1][1]
        arr.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < M and ny < N:
                if copy_lab[nx][ny] == 0:
                    copy_lab[nx][ny] = 2
                    arr.append([nx, ny])
    for i in copy_lab:
        for j in i:
            if j == 0:
                result += 1
    max_result = max(max_result, result)

# 벽
def wall(cnt):
    if cnt == 3:
        virus()
        return
    for i in range(M):
        for j in range(N):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(cnt+1)
                lab[i][j] = 0

M, N = map(int, input().split())
lab = [[] for _ in range(M)]
for i in range(M):
    lab[i] = list(map(int, input().split()))
wall(0)
print(max_result)