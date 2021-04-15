T = int(input())
for i in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    minNum = 1000000
    maxNum = 0
    for number in numbers:
        if number < minNum:
            minNum = number
        if number > maxNum:
            maxNum = number

    print(f'#{i} {maxNum-minNum}')
