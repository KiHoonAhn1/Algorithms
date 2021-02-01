S = int(input())
for i in range(S):
    R, P = input().split()
    R = int(R)
    for j in P:
        print(j * R, end='')
    print()