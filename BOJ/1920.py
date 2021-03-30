import sys

N = int(input())
arr1 = list(map(int, sys.stdin.readline().split()))
arr1.sort()

M = int(input())
arr2 = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    start = 0
    end = N-1
    while True:
        if arr2[i] > arr1[(start+end)//2]:
            start = (start+end)//2 + 1
        elif arr2[i] < arr1[(start+end)//2]:
            end = (start+end)//2 - 1
        elif arr2[i] == arr1[(start+end)//2]:
            print(1)
            break
        if start > end:
            print(0)
            break