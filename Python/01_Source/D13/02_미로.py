'''
1일 때 통로
'''

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    if arr[r][c] == 1:
        arr[r][c] = 2
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if arr[nr][nc] == 0 or arr[nr][nc] == 2:
            continue

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            dfs(i, j)
