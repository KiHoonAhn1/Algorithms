import sys

N = int(sys.stdin.readline())
arr = [0] * 10001
for i in range(N):
    arr[int(sys.stdin.readline())] += 1

for k in range(len(arr)):
    for x in range(arr[k]):
        print(k)
