T = int(input())
for tc in range(1, T+1):
    N = int(input())
    time = []
    for _ in range(N):
        time.append(list(map(int, input().split())))
    time = sorted(time, key = lambda x: (x[1], x[0]))

    max_result = 0
    for i in range(N):
        end = time[i][1]
        result = 1
        for j in range(i, N):
            if time[j][0] >= end:
                end = time[j][1]
                result += 1
            if max_result >= result + N - j - 1:
                break
            max_result = max(max_result, result)
    print(f'#{tc} {max_result}')