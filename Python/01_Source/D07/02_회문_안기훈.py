T = int(input())
for tc in range(1, T+1):
    arr = []
    N, M = map(int, input().split())
    for i in range(N):
        smallArr = []
        A = input()
        for j in A:
            smallArr.append(j)
        arr.append(smallArr)

    palindrome = False
    result = []
    # 가로
    for i in range(N):
        R = int(M//2)
        for k in range(N - M + 1):
            for j in range(R):
                if arr[i][k + j] != arr[i][M + k - j - 1]:
                    break
                if j == R-1 and arr[i][k + j] == arr[i][M + k - j - 1]:
                    palindrome = True
                    result = arr[i][k:k+M]
            if palindrome:
                print(f'#{tc} {"".join(result)}')
                break
        if palindrome == True:
            palindrome = False
            break

    # 세로
    for i in range(N):
        R = int(M//2)
        for k in range(N - M + 1):
            for j in range(R):
                if arr[k + j][i] != arr[M + k - j - 1][i]:
                    break
                if j == R-1 and arr[k + j][i] == arr[M + k - j - 1][i]:
                    palindrome = True
                    for x in range(M):
                        result.append(arr[k+x][i])
            if palindrome:
                print(f'#{tc} {"".join(result)}')
                break
        if palindrome == True:
            break