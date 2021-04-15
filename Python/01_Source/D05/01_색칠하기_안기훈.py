T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        square = list(map(int, input().split()))
        x1, y1, x2, y2 = square[0:4]
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if grid[i][j] == 0 or grid[i][j] == square[4]:
                    grid[i][j] = square[4]
                else:
                    grid[i][j] += square[4]

    cnt = 0
    for a in range(len(grid)):
        for b in grid[a]:
            if b == 3:
                cnt += 1
    print(f'#{tc} {cnt}')
