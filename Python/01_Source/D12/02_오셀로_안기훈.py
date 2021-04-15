T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    # 처음 돌 놓기
    board[N//3][N//3+1], board[N//3+1][N//3] = 1, 1 # 흑돌
    board[N//3][N//3], board[N//3+1][N//3+1] = 2, 2 # 백돌
    for i in range(M):
        x, y, stone = map(int, input().split())
        # 좌표 맞춰주기
        x, y = x-1, y-1
        board[y][x] = stone
        # 가로 왼쪽
        for j in range(x+1, N):
            occello = False
            if board[y][j] == stone:
                if stone == 1:
                    for k in range(x+1, j):
                        if board[y][k] == 1:
                            occello = False
                            break
                        else:
                            occello = True
                elif stone == 2:
                    for k in range(x+1, j):
                        if board[y][k] == 2:
                            occello = False
                            break
                        else:
                            occello = True
            if occello:
                for a in range(x+1, j):
                    board[y][a] = stone
                break
        # 가로 오른쪽
        for j in range(x):
            occello = False
            if board[y][j] == stone:
                if stone == 1:
                    for k in range(j+1, x):
                        if board[y][k] == 1:
                            occello = False
                            break
                        else:
                            occello = True
                elif stone == 2:
                    for k in range(j+1, x):
                        if board[y][k] == 2:
                            occello = False
                            break
                        else:
                            occello = True
            if occello:
                for a in range(j+1, x):
                    board[y][a] = stone
                break
        # 세로 위
        for j in range(y+1, N):
            occello = False
            if board[j][x] == stone:
                if stone == 1:
                    for k in range(y+1, j):
                        if board[k][x] == 1:
                            occello = False
                            break
                        else:
                            occello = True
                elif stone == 2:
                    for k in range(y+1, j):
                        if board[k][x] == 2:
                            occello = False
                            break
                        else:
                            occello = True
            if occello:
                for a in range(y+1, j):
                    board[a][x] = stone
                break
        # 세로 아래
        for j in range(y):
            occello = False
            if board[j][x] == stone:
                if stone == 1:
                    for k in range(j+1, y):
                        if board[k][x] == 1:
                            occello = False
                            break
                        else:
                            occello = True
                elif stone == 2:
                    for k in range(j+1, y):
                        if board[k][x] == 2:
                            occello = False
                            break
                        else:
                            occello = True
            if occello:
                for a in range(j+1, y):
                    board[a][x] = stone
                break

        # 대각선 위에서 오른쪽으로
        r = 0
        while x+r <= N or y+r <= N:
            if x+r > N or y+r > N:
                break
            elif board[y+r][x+r] != stone and board[y+r][x+r] != 0:
                pass
            elif board[y+r][x+r] == stone:
                break
            else:
                r = 0
                break
            r += 1

        for a in range(1, r):
            board[y+a][x+a] = stone

        # 대각선 위에서 왼쪽으로
        l = 0
        while x-l > 0 or y+l <= N:
            if x-l < 0 or y+l > N:
                break
            elif board[y+l][x-l] != stone and board[y+l][x-l] != 0:
                pass
            elif board[y+l][x-l] == stone:
                break
            else:
                l = 0
                break
            l += 1
        for a in range(1, l):
            board[y+a][x-a] = stone
            
        # 대각선 밑에서 오른쪽으로
        r = 0
        while x+r <= N or y-r > 0:
            print(x+r, N, y-r)
            if x+r > N or y-r < 0:
                break
            elif board[y-r][x+r] != stone and board[y-r][x+r] != 0:
                pass
            elif board[y-r][x+r] == stone:
                break
            else:
                r = 0
                break
            r += 1

        for a in range(1, r):
            board[y-a][x+a] = stone

        # 대각선 밑에서 왼쪽으로
        l = 0
        while x-l >= 0 or y-l >= 0:
            if x-l < 0 or y-l < 0:
                break
            elif board[y-l][x-l] != stone and board[y-l][x-l] != 0:
                print('왼쪽위')
            elif board[y-l][x-l] == stone:
                break
            else:
                l = 0
                break
            l += 1
            print('왼쪽위', l)
        for a in range(1, l):
            board[y-a][x-a] = stone


    # 바둑판 확인용
    for row in board:
        print(row)
    a_tot, b_tot = 0, 0
    for row in board:
        for i in row:
            if i == 1:
                a_tot += 1
            elif i == 2:
                b_tot += 1
    print(a_tot, b_tot)