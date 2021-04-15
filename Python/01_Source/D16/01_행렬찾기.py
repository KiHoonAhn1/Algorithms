def chemi(r, c, warehouse):
    arr = [1, 0]
    for i in range(r, N):
        for j in range(c, N):
            if warehouse[i][j] != 0:
                warehouse[i][j] = 0
                arr[1] += 1
            else:
                break
        if warehouse[i+1][j-1] == 0:
            arr[1] //= arr[0]
            return arr
        else:
            arr[0] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(N)]
    case = []

    for i in range(N):
        for j in range(N):
            if warehouse[i][j] != 0:
                case.append(chemi(i, j, warehouse))

    result = []
    for i in range(len(case)):
        minArea = 10000000
        minIdx = 0
        for j in range(len(case)):
            if case[j][0] * case[j][1] < minArea:
                minArea = case[j][0] * case[j][1]
                minIdx = j
            elif case[j][0] * case[j][1] == minArea:
                if case[minIdx][0] > case[j][0]:
                    minIdx = j
        result.append(case[minIdx][0])
        result.append(case[minIdx][1])
        case.pop(minIdx)

    print(f'#{tc} {len(result)//2} {" ".join(map(str, result))}')