def dfs(n):
    stack = [0] * 100000
    visited = [0] * (V + 1)
    top = -1

    top += 1
    stack[top] = n

    while top >= 0:
        if stack[top] == G:
            return True
        cur = stack[top]
        top -= 1
        if visited[cur] == 0:
            visited[cur] = 1

        for i in range(1, V+1):
            if adj[cur][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i
    return False

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
    S, G = map(int, input().split())

    if dfs(S):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
