'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(n): # 현재 노드
    # 준비 작업
    stack = [0] * V # 스택
    visited = [0] * (V + 1) # 방문배열
    top = -1 # top 표시
    
    # 시작정점 처리
    top += 1
    stack[top] = n

    while top >= 0:
        cur = stack[top] # 스택에서 하나를 꺼내옴
        top -= 1

        if visited[cur] == 0:
            print(cur, end=' ')
            visited[cur] = 1


        for i in range(1, V+1): # 현재 정점에서 인접한 정점을 탐색
            if adj[cur][i] == 1 and visited[i] == 0:
                top += 1
                stack[top] = i


V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0 for _ in range(V + 1)] for _ in range(V+1)]
for i in range(E): # 간선의 수 만큼 반복
    n1, n2 = edge[i*2], edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1