T = int(input())
for tc in range(1, T+1):
    C, T = map(int, input().split())
    containers = list(map(int, input().split()))
    containers.sort()
    trucks = list(map(int, input().split()))
    trucks.sort()
    result = 0
    visited = [0 for _ in range(C)]

    for truck in trucks:
        idx = 100
        for i in range(C):
            if i == C-1:
                if visited[C-1] == 0:
                    result += containers[i]
                    visited[i] = 1
                else:
                    result += containers[idx]
                    visited[idx] = 1
                break

            if truck < containers[i]:
                if idx != 100:
                    result += containers[idx]
                    visited[idx] = 1
                break
            if visited[i] == 0:
                idx = i
    print(f'#{tc} {result}')