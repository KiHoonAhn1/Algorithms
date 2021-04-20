def backtrack(idx, cnt):
    global min_cnt
    if cnt > min_cnt:
        return

    if idx + stations[idx] >= N-1:
        min_cnt = min(cnt, min_cnt)
        return

    for i in range(1, stations[idx]+1):
        backtrack(idx+i, cnt+1) if idx + i < N else ''

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N, stations = arr[0], arr[1:]
    min_cnt = 987654321
    backtrack(0, 0)
    print(f'#{tc} {min_cnt}')