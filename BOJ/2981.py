import sys

def gcd(A, B):
    result = A*B
    remain = 0
    while True:
        remain = A % B
        if remain == 0:
            break
        A = B
        B = remain
    return B

#arr.sort()
N = int(sys.stdin.readline().rstrip())
arr = sorted([int(input()) for _ in range(N)])

diff_arr = [0]*(N-1)
for i in range(N-1):
    diff_arr[i] = arr[i+1] - arr[i]

while len(diff_arr) != 1:
    diff_arr.append(gcd(diff_arr.pop(), diff_arr.pop()))

res = set()
for i in range(1, int(diff_arr[0]**0.5)+1):
    if not diff_arr[0] % i:
        res.add(i)
        res.add(diff_arr[0] // i)
res = sorted(list(res))
res.remove(1)
print(' '.join(map(str, res)))