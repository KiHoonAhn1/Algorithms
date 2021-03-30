import sys

N = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))

M = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

dic = dict()

for i in arr1:
    try :
        dic[i] += 1
    except:
        dic[i] = 1

for i in arr2:
    try:
        print(dic[i] , end = " ")
    except:
        print(0, end=" ")