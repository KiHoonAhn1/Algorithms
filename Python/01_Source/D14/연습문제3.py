'''
1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

- 1- 2- 3- 4- 5- 7 - 6
'''
'''
def bfs(G, v):
    visited = [0] * N
    queue = []
    queue.append(v)
    while queue:
        t = queue.pop()
        if not visited[t]:
            visited[t] = 1
        for i in G[t]:
            if not visited[i]:
                queue.append(i)

arr = list(map(int, '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'.split()))

N = 7
G = []
for i in range(len(arr)//2):
    G.append([arr[i*2], arr[i*2+1]])
bfs(G, 1)
'''

'''
큐 생성
시작정점을 큐에 삽입
시작정점을 방문했다고 표시

큐에서 정점 cur을 꺼내옴
정점 cur에 인접한 정점 v를 큐에 넣음
v를 방문했다고 표시
'''

def bfs(n): # n : 시작 정점
    visited = [0] * (V+1) # 방문배열 -> 정점의 갯수만큼 생성, 0으로 초기화, 방문하면 1
    q = []
    q.append(n)
    visited[n] = 1

    while q:
        cur = q.pop(0) # 큐에서 하나 꺼내옴
        print(cur, end=' ') # 현재 정점 출력
        for v in range(1, V+1):
            if adj[cur][v] == 1 and visited[v] == 0: # 정점 cur에 인접하고 아직 방문하지 않은 v
                q.append(v) # 인접 정점을 큐에 넣음
                visited[v] = 1 # 큐에 삽입하면서 방문표시



# 입력 확인
# 그래프의 표현 : 인접행렬, 인접리스트
# 탐색기법선정 -> bfs
# bfs
# 방문 배열 생성
# 시작정점을 기준으로 vfs 탐색

V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0 for _ in range(V+1)] for _ in range(V+1)] # 정점 크기 * 정점 크기의 행렬
for i in range(E):
    n1, n2 = edge[i*2], edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1


bfs(1)
