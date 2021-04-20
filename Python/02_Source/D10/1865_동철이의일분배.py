def backtrack(idx, total):
    global max_percentage
    if total <= max_percentage:
        return
    if idx == N:
        max_percentage = max(total, max_percentage)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            backtrack(idx+1, total*percent[idx][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            percent[i][j] = percent[i][j] / 100
    visited = [0 for _ in range(N)]
    max_percentage = 0
    backtrack(0, 100)
    print('#%d %0.6f' % (tc, round(max_percentage, 6)))