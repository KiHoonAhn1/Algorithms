T = int(input())
for tc in range(T):
    N = int(input())
    if N < 4:
        arr = [1] * N
    else:
        arr = [1, 1, 1] + [0] * (N-3)
    for i in range(3, N):
        arr[i] = arr[i-2] + arr[i-3]
    print(arr[N-1])