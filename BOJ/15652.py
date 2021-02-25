def solve(cnt, N, M, arr):
    if cnt == M:
        print(*arr)
        return

    for i in range(1, N+1):
        sorted_arr = True
        for j in arr:
            if i < j:
                sorted_arr = False
                break
        if sorted_arr:
            arr.append(i)
            solve(cnt+1, N, M, arr)
            arr.pop()

N, M = map(int, input().split())
arr = []
solve(0, N, M, arr)