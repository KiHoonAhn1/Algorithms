N = int(input())
arr = []
dp = []
for _ in range(N):
    arr.append(int(input()))

if N == 1:
    print(arr[0])
elif N == 2:
    print(arr[0]+arr[1])
elif N == 3:
    print(max(arr[0]+arr[1], arr[1]+arr[2]))
else:
    dp.append(arr[0])
    dp.append(arr[0]+arr[1])
    dp.append(max(arr[0]+arr[2], arr[1]+arr[2]))
    dp.append(max(arr[0] + arr[1] + arr[3], arr[0] + arr[2] + arr[3]))
    for i in range(4, N):
        dp.append(max(dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-4]+arr[i-1]+arr[i]))
    print(max(dp))
