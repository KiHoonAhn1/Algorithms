T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
    w = [0] + [987654321 for _ in range(V)]
    result = 0
    for i in range(V+1):
        for j in range(V+1): # i에서 j로
            if adj[i][j]:
                if w[j] > w[i] + adj[i][j]:
                    w[j] = w[i] + adj[i][j]
    print(f'#{tc} {w[V]}')
