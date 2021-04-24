T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split()) # N개의 집, X번이 목적지, M개에 걸쳐 길
    road = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        road[a][b] = c
    w1 = [987654321 for _ in range(N+1)] # X번에서 각각의 집으로
    w2 = [987654321 for _ in range(N+1)] # 각각의 집에서 X번으로
    for i in range(1, N+1):
        for j in range(1, N+1): # i에서 j로
            if road[i][j]:
                if w[j] > w[i] + adj[i][j]:
                    w[j] = w[i] + adj[i][j]

#
# 병합정렬 동철이일분배 홈워크 이분탐색 입국심사 뭔가 늘어나고잇어
# 베이비진, 최장경로, 최소 이동 거리, 프로그래머스 이문탐색 입국심사
#
# homework 위주, 이분탐색, 입국심사