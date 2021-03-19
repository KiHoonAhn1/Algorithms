import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1 for _ in range(N)]


for i in range(N):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

for j in result:
    print(j, end=" ")