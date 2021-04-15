for i in range(1, 11):
    N = int(input())
    rooms = list(map(int, input().split()))
    count = 0
    for j in range(N):
        while True:
            if rooms[j] > rooms[j-1] and rooms[j] > rooms[j-2] and rooms[j] > rooms[j+1] and rooms[j] > rooms[j+2]:
                count += 1
                rooms[j] -= 1
            else:
                break
    print(f'#{i} {count}')