import copy

M, N = map(int, input().split())
arr = []
Oarr = []
color = ['W', 'B']
for m in range(M):
    Oarr.append(list(input()))

minCnt = 1500
for a in range(2):
    x, y = 0, 0
    while y < M-7:
        cnt = 0
        arr = copy.deepcopy(Oarr)
        if a == 0 and arr[y][x] == 'B':
            cnt += 1
        elif a == 1 and arr[y][x] == 'W':
            cnt += 1
        arr[y][x] = color[a]
        for i in range(y, 8+y):
            if i != y and arr[i-1][x] == arr[i][x]:
                cnt += 1
                if arr[i-1][x] == 'B':
                    arr[i][x] = 'W'
                elif arr[i-1][x] == 'W':
                    arr[i][x] = 'B'
            for j in range(x, 7+x):
                if arr[i][j] == arr[i][j+1]:
                    cnt += 1
                    if arr[i][j] == 'B':
                        arr[i][j+1] = 'W'
                    elif arr[i][j] == 'W':
                        arr[i][j+1] = 'B'
        if cnt < minCnt:
            minCnt = cnt
        x += 1
        if x == N-7:
            x = 0
            y += 1

print(minCnt)