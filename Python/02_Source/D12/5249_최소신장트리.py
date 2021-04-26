def find_parent(n):
    if p[n] != n:
        p[n] = find_parent(p[n])
    return p[n]

def union(n1, n2):
    pn1 = find_parent(n1)
    pn2 = find_parent(n2)

    if pn1 < pn2:
        p[pn1] = pn2
    else:
        p[pn2] = pn1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0, 0, 0] for _ in range(E)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[i] = [n1, n2, w]
    adj = sorted(adj, key = lambda x: x[2])

    p = [i for i in range(V+1)]
    result = 0
    for n1, n2, w in adj:
        if find_parent(n1) != find_parent(n2):
            union(n1, n2)
            result += w
    print(f'#{tc} {result}')



'''T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w
    w = [0] + [987654321 for _ in range(V)]
    p = [i for i in range(V+1)]
    result = 0
    for i in range(V+1):
        for j in range(V+1): # i에서 j로
            if adj[i][j]:
                print(i, j, w[j], w[i])
                if w[j] > w[i] + adj[i][j]:
                    while i != p[j]:
                        p[j] = i
                    w[j] = w[i] + adj[i][j]
    for i in range(V+1):
        result += adj[i][p[i]]
    print(result)
'''