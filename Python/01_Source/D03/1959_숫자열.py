T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    AList = list(map(int, input().split()))
    BList = list(map(int, input().split()))
    maxNum = 0
    if len(AList) < len(BList):
        for i in range(M - N + 1):
            total = 0
            BList1 = BList[i:i+N]
            for j in range(N):
                total += AList[j] * BList1[j]
            if maxNum < total:
                maxNum = total
    elif len(AList) > len(BList):
        for i in range(N - M + 1):
            total = 0
            AList1 = AList[i:i+M]
            for j in range(M):
                total += BList[j] * AList1[j]
            if maxNum < total:
                maxNum = total
    print(f'#{tc} {maxNum}')
