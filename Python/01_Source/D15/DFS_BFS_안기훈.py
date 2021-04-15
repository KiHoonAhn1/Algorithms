def bfs(V):
    visited = [0] * (N + 1)
    queue = []
    queue.append(V)
    visited[V] = 1

    while queue:
        t = queue.pop(0)
        print(t, end=' ')
        for i in range(1, V+1):
            if visited[i] == 0 and adj[t][i] == 1:
                visited[i] = 1
                queue.append(i)


def dfs(V):
    stack = [0] * N
    visited = [0] * N
    top = -1

    top += 1
    stack[top] = V

    while top >= 0:
        cur = stack[top]
        top -= 1
        if visited[cur] == 0:
            print(cur, end=' ')
            visited[cur] = 1

        for i in range(1, V+1):
            if adj[cur][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i


N, M, V = map(int, input().split())
adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1
dfs(V)
bfs(V)
