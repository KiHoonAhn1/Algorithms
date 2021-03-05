def fibonacci(N, d):
    if N == 0:
        d[0][0] = 1
    elif N == 1:
        d[1][1] = 1
    else:
        d[0][0] = 1
        d[1][1] = 1
        for i in range(2, N+1):
            d[0][i] = d[0][i-1] + d[0][i-2]
            d[1][i] = d[1][i-1] + d[1][i-2]

T = int(input())
for tc in range(T):
    N = int(input())
    d = [[0 for _ in range(N+1)] for _ in range(2)]
    fibonacci(N, d)
    print(d[0][N], d[1][N])