import sys

N = int(sys.stdin.readline())
color = [[0]*3 for _ in range(N)]
for i in range(N):
    color[i] = (list(map(int, sys.stdin.readline().split())))

result = 0

for i in range(1, N):
    minNum = 1000
    for j in range(3):
            color[i][j] = min(color[i][j]+color[i-1][j-1], color[i][j]+color[i-1][j-2])
if N == 1:
    print(min(color[i]))
else:
    print(min(color[N-1]))