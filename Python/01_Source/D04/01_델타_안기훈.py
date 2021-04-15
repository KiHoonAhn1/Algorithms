'''
2 7 4 3 6
8 5 8 3 2
2 2 3 6 9
5 9 2 5 7
3 6 2 9 4
'''
arr = [list(map(int, input().split())) for _ in range(5)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
results = [[0] * 5 for _ in range(5)]

for i in range(5):
    for j in range(5):
        r = i
        c = j
        result = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if r == 4 and dr[k] > 0:
                answer = 0
            elif c == 4 and dc[k] > 0:
                answer = 0
            elif r == 0 and dr[k] < 0:
                answer = 0
            elif c == 0 and dc[k] < 0:
                answer = 0
            else:
                answer = arr[r][c] - arr[nr][nc]

            if answer < 0:
                answer = -answer

            result += answer
        results[r][c] = result
print(results)