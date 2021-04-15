T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    result = [0]
    for i in range(N):
        copy_result = []
        for j in result:
            if j+scores[i] not in result:
                copy_result.append(scores[i]+j)

        for k in copy_result:
            result.append(k)

    print(f'#{tc} {len(result)}')