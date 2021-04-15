def dfs(idx, result):
    global minResult
    if idx == N:
        if minResult > result:
            minResult = result
        return

    if result > minResult:
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx+1, result+arr[idx][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    minResult = 999999999
    dfs(0, 0)
    print(f'#{tc} {minResult}')