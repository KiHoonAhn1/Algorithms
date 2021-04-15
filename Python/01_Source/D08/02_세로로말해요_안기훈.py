T = int(input())
for tc in range(1, T+1):
    arr = [[0 for _ in range(15)] for _ in range(5)]
    A = [input() for _ in range(5)]

    for i in range(5):
        for j in range(len(A[i])):
            arr[i][j] = A[i][j]

    empty_string = ''
    for j in range(15):
        for i in range(5):
            if arr[i][j] != 0:
                empty_string += arr[i][j]

    print(f'#{tc} {empty_string}')