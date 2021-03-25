import sys

N = int(sys.stdin.readline())
arr = list(map(int, input().split()))
dp = [0]
numdp = [0]
cnt = 0
temp = []
for i in range(N):
    if numdp[-1] < arr[i]:
        dp.append(i)
        numdp.append(arr[i])
    elif numdp[-1] > arr[i]:
        cnt = numdp.index(arr[i])
        temp.append(i)


        30 50 20 30 40
