import sys

N = int(sys.stdin.readline())
non = [4, 7]
x3 = [3, 6, 9, 12]
x5 = [5, 10, 15]
x3x5 = [8, 11, 13, 14, 16, 17]
another = [1, 2, 4, 7]

A = N % 15

if N in non:
    print(-1)
else:
    if A in x3:
        print(N//15*3 + A//3)
    elif A in x5 or A == 0:
        print(N//15*3 + A//5)
    else:
        if A == 8:
            print(N//15*3 + 1 + (A-5)//3)
        elif A == 13:
            print(N//15*3 + 2 + (A-10)//3)
        elif A == 1 or A == 4 or A == 7:
            print(((N//15)-1)*3 + 2 + (A+5)//3)
        elif A == 2:
            print(((N//15)-1)*3 + 1 + (A+10)//3)
        else:
            print(N//15*3 + 1 + (A-5)//3)

# 3 6 9 12
#  5   10
#    8  11 13 14
# 1, 2, 4, 7