def relationship(idx):
    for j in range(1, N+1):
        if people[idx][j] and not visited[j]:
            visited[j] = 1
            relationship(j)

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N번 사람까지, M 번에 걸쳐서 관계를 알려줌
    people = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(M):
        arr = list(map(int, input().split()))
        if len(arr) == 2:
            a, b = arr[0], arr[1]
            people[a][b] = 1
            people[b][a] = 1

    visited = [0 for _ in range(N+1)]
    cnt = 0
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            relationship(i)
    print(f'#{tc} {cnt}')