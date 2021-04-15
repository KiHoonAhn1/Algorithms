T = int(input())
for tc in range(1, T+1):
    A = input()
    B = input()
    arr = [0 for _ in range(len(A))]
    for a in range(len(A)):
        for b in B:
            if A[a] == b:
                arr[a] += 1

    maxNum = 0
    for i in arr:
        if i > maxNum:
            maxNum = i

    print(f'#{tc} {maxNum}')