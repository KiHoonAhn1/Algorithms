min_result = 1000000

def chicken():
    print(city)

def close(count, i ,j):
    if count == cnt - M:
        print(i, j, count)
        chicken()
        return
    for i in range(N):
        for j in range(N):
            if city[i][j] == 2:
                city[i][j] = 0
                close(count + 1, i, j)
                city[i][j] = 2

N, M = map(int, input().split())
city = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
for i in range(N):
    city[i] = list(map(int, input().split()))
    for j in range(N):
        if city[i][j] == 2:
            cnt += 1
close(0, 0, 0)