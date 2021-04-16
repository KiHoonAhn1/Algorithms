money = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    count = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(len(money)):
        if i == 0:
            count[i] = N // money[i]
        else:
            ratio = money[i] // money[i-1]
            if count[i-1] < ratio:
                break
            else:
                count[i] = count[i-1] // ratio
                count[i-1] = count[i-1] % ratio
    print(f'#{tc}')
    for cnt in count[::-1]:
        print(cnt, end=' ')
    print()