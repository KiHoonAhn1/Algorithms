import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    num_list = list(map(int, sys.stdin.readline().split()))
    arr.append(num_list)
    if i == 0:
        continue
    for j in range(len(num_list)):
        if j == 0:
            arr[i][0] += arr[i-1][0]
        elif j == len(num_list)-1:
            arr[i][len(num_list)-1] += arr[i-1][len(num_list)-2]
        else:
            arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

print(max(arr[N-1]))