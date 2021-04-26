def dijkstra(start, X):
    queue = []
    queue.append([0, start])
    w = [987654321 for _ in range(N+1)]
    w[start] = 0

    i = -1
    while i != len(queue)-1:
        i += 1
        temp = queue[i]

        for v in range(1, N+1):
            if not road[temp[1]][v]:
                continue
            if w[v] > temp[0] + road[temp[1]][v]:
                w[v] = temp[0] + road[temp[1]][v]
                queue.append([w[v], v])

    if start != X:
        return w[X]
    else:
        return w

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # N개의 집, X번이 목적지, M개에 걸쳐 길
    road = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        road[a][b] = c
    result = [0 for _ in range(N+1)] # 각각의 집에서 X로
    fromX = [] # X에서 각각의 집으로

    for i in range(1, N+1):
        if i == X:
            fromX = dijkstra(i, X)
        else:
            result[i] = dijkstra(i, X)

    for j in range(1, N+1):
        result[j] += fromX[j]

    print(f'#{tc} {max(result)}')

#
# 병합정렬 동철이일분배 홈워크 이분탐색 입국심사 뭔가 늘어나고잇어
# 베이비진, 최장경로, 최소 이동 거리, 프로그래머스 이문탐색 입국심사
#
# homework 위주, 이분탐색, 입국심사