def solve(cnt, N, M, arr):
    if cnt == M:
        if arr == sorted(arr):
            print(*arr)
            return
        else:
            return
    else:
        for i in range(1, N+1):
            if i in arr:
                continue
            else:
                arr.append(i)
                solve(cnt+1, N, M, arr)
                arr.pop()

N, M = map(int, input().split())
arr = []
solve(0, N, M, arr)