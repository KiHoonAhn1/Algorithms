'''
N, K = map(int, input().split())
if K == 0:
    print(1)
else:
    A, B = 1, 1
    for i in range(K):
        A *= N
        N -= 1

    for j in range(K):
        B *= K
        K -= 1
    print((A//B)%10007)
'''
N, K = map(int, input().split())
dp = [[0] for i in range(1001)]
for i in range(2, 1001):
    for j in range(1, i+1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i-1][j-1]+dp[i-1][j])
print(dp[N+1][K+1] % 10007)