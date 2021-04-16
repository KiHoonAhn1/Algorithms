dx = [0, 1]
dy = [1, 0]
def min_board(x, y, total):
    global min_result
    if x == N-1 and y == N-1:
        min_result = min(min_result, total)
        return
    if min_result < total:
        return

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < N and ny < N:
            min_board(nx, ny, total + board[nx][ny])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        board[i] = list(map(int, input().split()))
    min_result = 987654321
    min_board(0, 0, board[0][0])
    print(f'#{tc} {min_result}')
