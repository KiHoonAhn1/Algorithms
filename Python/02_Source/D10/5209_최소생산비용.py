def backtrack(idx, price, visited):
    global min_price
    if price > min_price:
        return

    if idx == N:
        min_price = min(price, min_price)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtrack(idx+1, price+factory[idx][i], visited)
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    factory = [list(map(int, input().split())) for _ in range(N)]
    min_price = 987654321
    visited = [0 for _ in range(N)]
    backtrack(0, 0, visited)
    print(f'#{tc} {min_price}')