def BFS(N, M):
    f = r = -1
    visited[N] = 1

    r += 1
    queue[r] = N
    while f != r:
        f += 1
        n = queue[f]

        next_n = [n + 1, n - 1, n * 2, n - 10]
        for i in range(4):
            if next_n[i] == M:
                return visited[n]

            if 0 < next_n[i] <= 1000000 and not visited[next_n[i]]:
                visited[next_n[i]] = visited[n] + 1
                r += 1
                queue[r] = next_n[i]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = [0] * 1000001
    queue = [0] * 1000000
    result = BFS(N, M)
    print(f'#{tc} {result}')


'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    queue = [(M, 0)]
    while queue:
        temp = queue.pop(0)
        if temp[0] == N:
            break
        else:
            # // 2
            if temp[0] % 2 == 0 and temp[0] // 2 > 1 and not visited[temp[0] // 2]:
                visited[temp[0] // 2] = 1
                queue.append((temp[0]//2, temp[1] + 1))
            # + 10
            if temp[0] + 10 <= 1000000 and not visited[temp[0] + 10]:
                visited[temp[0] + 10] = 1
                queue.append((temp[0]+10, temp[1]+1))
            # + 1
            if temp[0] + 1 <= 1000000 and not visited[temp[0] + 1]:
                visited[temp[0] + 1] = 1
                queue.append((temp[0]+1, temp[1]+1))
            # -1
            if temp[0] - 1 > 0 and not visited[temp[0] - 1]:
                visited[temp[0] - 1] = 1
                queue.append((temp[0]-1, temp[1]+1))

    print(f'#{tc} {temp[1]}')
'''