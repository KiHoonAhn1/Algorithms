dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def check_board(x, y, arr, cnt):
    if cnt == 7:
        numbers.add(arr)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < 4 and ny < 4:
            check_board(nx, ny, arr+str(board[nx][ny]), cnt+1)

T = int(input())
for tc in range(1, T+1):
    board = [[] for _ in range(4)]
    numbers = set()
    for i in range(4):
        board[i] = list(map(int, input().split()))

    for i in range(4):
        for j in range(4):
            check_board(i, j, str(board[i][j]), 1)

    print(f'#{tc} {len(numbers)}')