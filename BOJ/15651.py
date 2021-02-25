def solve(cnt, N, M, arr):
    if cnt == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(1, N+1):
        arr.append(i)
        solve(cnt+1, N, M, arr)
        arr.pop()

N, M = map(int, input().split())
arr = []
solve(0, N, M, arr)