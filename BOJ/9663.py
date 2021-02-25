# def chess(N, cnt, arr):
    # for i in range(N):
        # pass


N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    arr[i][0] = 1
    arr[0][i] = 1
    arr[i][i] = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cnt = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            arr[i][j] == 1

            for k in range(4):
                ni = i + dr[k]
                nj = j + dc[k]
                while ni >= 0 and ni < N and nj >= 0 and nj < N:
                    arr[ni][nj] = 1
                    ni = ni + dr[k]
                    nj = nj + dc[k]

for row in arr:
    print(row)