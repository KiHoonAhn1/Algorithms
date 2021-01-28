import copy

N = input()
if int(N) < 10:
    N = '0' + N
B = copy.deepcopy(N)
count = 0
while True:
    count += 1
    A = int(B[0]) + int(B[1])
    B = B[-1] + str(A)[-1]
    if N == B:
        print(count)
        break