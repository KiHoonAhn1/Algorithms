def team(idx):
    for i in range(1, N+1):
        if visited[i] == 0 and adj[idx][i] == 1:
            visited[i] = 1
            team(i)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N까지 출석 번호, M 장의 신청서
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]
    arr = list(map(int, input().split()))
    for i in range(M):
        adj[arr[i*2]][arr[i*2+1]] = 1
        adj[arr[i*2+1]][arr[i*2]] = 1
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            team(i)
            cnt += 1

    print(f'#{tc} {cnt}')