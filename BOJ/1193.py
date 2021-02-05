import sys

N = int(sys.stdin.readline())

a = 1
while True:
    total = round(a * (a + 1) / 2)
    if total >= N:
        if a % 2:
            print(f'{1+(total-N)}/{a-(total-N)}')
            break
        else:
            print(f'{a-(total-N)}/{1+(total-N)}')
            break
    else:
        a += 1