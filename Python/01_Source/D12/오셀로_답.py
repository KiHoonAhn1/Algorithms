'''
1
4 12
1 2 1
1 1 2
4 3 1
4 4 2
2 1 1
4 2 2
3 4 1
1 3 2
2 4 1
1 4 2
4 1 2
3 1 2
'''
# 가로, 세로, 대각선 탐색을 위한 델타
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def check(i, j, color):
    for k in range(8):
        ni, nj = i + dr[k], j + dc[k]
        changeList = [] # 변경할 좌표 리스트
        needToChange = False # 변경 여부 저장
        while ni >= 0 and ni < N and nj >= 0 and nj < N: # 탐색 위치가 보드안일 동안
            if board[ni][nj] == 0: # 돌이 없으면
                break
            if board[ni][nj] == color:
                needToChange = True
                break
            else:
                changeList.append([ni, nj])
                ni = ni + dr[k]
                nj = nj + dc[k]
        if needToChange and changeList:
            for c in changeList:
                board[c[0]][c[1]] = color

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 보드 크기, M: 돌 놓는 횟수
    board = [[0 for _ in range(N)] for _ in range(N)]
    center = N//2
    board[center-1][center-1] = 2
    board[center][center] = 2
    board[center-1][center] = 1
    board[center][center-1] = 1

    for k in range(M):
        j, i, color = map(int, input().split()) # 입력값이 열, 행, 돌색깔
        board[i-1][j-1] = color
        check(i-1, j-1, color) # 돌 색을 변경하기 위한 함수, 좌표, 돌 색 매개변수

    cnt_b = 0
    cnt_w = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt_b += 1
            elif board[i][j] == 2:
                cnt_w += 1
    print(f'#{tc}', cnt_b, cnt_w)
