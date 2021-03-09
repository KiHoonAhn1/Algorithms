import sys

N = int(sys.stdin.readline())
arr = [[0, 0] for _ in range(N)]
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    arr[i][0] = s
    arr[i][1] = e

arr = sorted(arr, key = lambda x : (x[1], x[0]))

cnt = 1
end_time = arr[0][1]
for j in range(1, N):
    if arr[j][0] >= end_time:
        cnt += 1
        end_time = arr[j][1]

print(cnt)