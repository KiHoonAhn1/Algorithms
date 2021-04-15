def specialArr(N, arr):
    sArr = []

    a, b = 0, 0
    while True:
        max = 0
        min = 101

        for i in range(len(arr)):
            if max <= arr[i]:
                max = arr[i]
                a = i
        sArr.append(str(max))
        arr.pop(a)

        for j in range(len(arr)):
            if arr[j] <= min:
                min = arr[j]
                b = j
        sArr.append(str(min))
        arr.pop(b)

        if len(sArr) == 10:
            return sArr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {(" ").join(specialArr(N, arr))}')
