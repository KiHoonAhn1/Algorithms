for _ in range(1, 11):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    maxNum = 0
    # 가로
    for i in range(len(arr)):
        for j in range(len(arr[i])-1):
            #짝수
            if arr[i][j] == arr[i][j+1]:
                num = 0
                a = b = j
                while True:
                    if a < 0 or b+1 > 99:
                        if num > maxNum:
                            maxNum = num
                        break

                    if arr[i][a] == arr[i][b+1]:
                        a -= 1
                        b += 1
                        num += 2
                    else:
                        if num > maxNum:
                            maxNum = num
                        break
            # 홀수
            if arr[i][j-1] == arr[i][j+1]:
                num = 1
                a = b = j
                while True:
                    if a-1 < 0 or b+1 > 99:
                        if num > maxNum:
                            maxNum = num
                        break

                    if arr[i][a-1] == arr[i][b+1]:
                        a -= 1
                        b += 1
                        num += 2
                    else:
                        if num > maxNum:
                            maxNum = num
                        break

    # 세로
    for i in range(len(arr)):
        for j in range(len(arr[i])-1):
            #짝수
            if arr[j][i] == arr[j+1][i]:
                num = 0
                a = b = j
                while True:
                    if a < 0 or b+1 > 99:
                        if num > maxNum:
                            maxNum = num
                        break

                    if arr[a][i] == arr[b+1][i]:
                        a -= 1
                        b += 1
                        num += 2
                    else:
                        if num > maxNum:
                            maxNum = num
                        break
            # 홀수
            if arr[j-1][i] == arr[j+1][i]:
                num = 1
                a = b = j
                while True:
                    if a-1 < 0 or b+1 > 99:
                        if num > maxNum:
                            maxNum = num
                        break

                    if arr[a-1][i] == arr[b+1][i]:
                        a -= 1
                        b += 1
                        num += 2
                    else:
                        if num > maxNum:
                            maxNum = num
                        break

    print(f'#{tc} {maxNum}')
