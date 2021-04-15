T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    minNum = 100000000000
    maxNum = 0

    for n in range(N-M+1):
        tot = 0
        for m in num_list[n:n+M]:
            tot += m
        if tot < minNum:
            minNum = tot
        if tot > maxNum:
            maxNum = tot
    print(f'#{i} {maxNum-minNum}')
