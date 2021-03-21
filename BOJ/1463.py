N = int(input())
dp = [0] * (10**6+1)
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, N+1):
    if i % 3 == 0 and i % 2 == 0:
        dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
    elif i % 3 == 0:
        dp[i] = min(dp[i//3], dp[i-1]) + 1
    elif i % 3:
        if i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
        else:
            dp[i] = dp[i-1] + 1
    elif i % 2 == 0:
        dp[i] = min(dp[i//2], dp[i-1]) + 1
    else:
        dp[i] = dp[i-1] + 1
print(dp[N])


# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
# 0 1 1 2 3 2 3 3 2 3  4  3  4  4  4  4
