def bfs(S):
    visited = [0] * (V + 1)
    queue = []
    result = [0] * (V + 1)
    queue.append(S)
    visited[S] = 1

    while queue:
        s = queue.pop(0)
        for i in range(1, V+1):
            if visited[i] == 0 and adj[s][i] == 1:
                queue.append(i)
                visited[i] = 1
                result[i] = result[s] + 1
                if i == G:
                    return result[i]
    return 0


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(S)}')
