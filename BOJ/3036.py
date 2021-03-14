remain = 0
def gcd(a, b):
    remain = a % b
    if remain == 0:
        return b
    else:
        return gcd(b, remain)

N = int(input())
rings = list(map(int, input().split()))
first = rings[0]
for i in rings[1:]:
    num = gcd(first, i)
    print(f'{int(first/num)}/{int(i/num)}')