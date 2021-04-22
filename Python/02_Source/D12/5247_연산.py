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