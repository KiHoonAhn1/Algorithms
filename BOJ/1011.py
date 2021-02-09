import math

N = int(input())
for _ in range(N):
    A, B = map(int, input().split())
    maxV = int(math.sqrt(B - A))

    num = 0
    location = 0
    # 2 * maxV - 1 은 딱 maxV까지 순차적으로 올라갔다가 내려올 때 까지의 횟수
    remain_location = (B - A) - maxV**2
    num += maxV * 2 - 1
    while True:
        if remain_location == 0:
            break
        else:
            for i in range(maxV, 0, -1):
                if remain_location >= i:
                    remain_location -= i
                    num += 1
    print(num)

    # 1 -> 1
    # 1 2 1 -> 4
    # 1 2 3 2 1 -> 9
    # 1 2 3 4 3 2 1 -> 16
    # 1 2 3 4 5 4 3 2 1 -> 25

