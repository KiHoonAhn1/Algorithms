import sys

N = int(sys.stdin.readline())
color = [[0]*3 for _ in range(N)]
for i in range(N):
    color[i] = (list(map(int, sys.stdin.readline().split())))

result = 0
idx = 3

for i in range(N):
    minPrice = 1000
    for j in range(3):
        if color[i][j] < minPrice:
            if idx == j:
                pass
            else:
                minPrice = color[i][j]
                idx = j
    result += minPrice

print(result)