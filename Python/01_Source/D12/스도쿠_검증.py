T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    sudoku = True
    # 가로
    for i in range(9):
        num_arr = []
        for j in range(9):
            if arr[i][j] in num_arr:
                sudoku = False
                break
            else:
                num_arr.append(arr[i][j])
        if not sudoku:
            break
    # 세로
    for i in range(9):
        num_arr = []
        for j in range(9):
            if arr[j][i] in num_arr:
                sudoku = False
                break
            else:
                num_arr.append(arr[j][i])
        if not sudoku:
            break

    # 3x3
    for x in range(3):
        for y in range(3):
            num_arr = []
            for i in range(x*3, 3+x*3):
                for j in range(y*3, 3+y*3):
                    if arr[i][j] in num_arr:
                        sudoku = False
                        break
                    else:
                        num_arr.append(arr[i][j])
                if not sudoku:
                    break

    if sudoku:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

