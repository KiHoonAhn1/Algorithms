def dfs(n):
    stack = []
    visited = [0] * (100)
    stack.append(n)

    while stack:
        cur = stack[-1]
        stack.pop()

        if visited[cur] == 0:
            visited[cur] = 1

        for i in range(100):
            if arr[cur][i] == 1 and visited[i] == 0:
                stack.append(i)
                if i == 99:
                    return 1
    return 0

for _ in range(10):
    T, N = map(int, input().split())
    arr = [[0 for _ in range(100)] for _ in range(100)]
    point = list(map(int, input().split()))
    for i in range(N):
        n1, n2 = point[i*2], point[i*2+1]
        arr[n1][n2] = 1
    print(dfs(1))
