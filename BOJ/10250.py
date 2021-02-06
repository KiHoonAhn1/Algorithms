import sys
import math

T = int(sys.stdin.readline())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    room = math.ceil(N / H)
    floor = N % H
    # 최고층인 경우(ex. 6층 중 6번째)
    if floor == 0:
        if room >= 10:
            print(f'{H}{room}')
        else:
            print(f'{H}0{room}')
    else:
        if room >= 10:
            print(f'{floor}{room}')
        else:
            print(f'{floor}0{room}')