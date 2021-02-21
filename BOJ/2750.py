import sys

N = int(sys.stdin.readline())
arr = []
for x in range(N):
    arr.append(int(input()))

preNum = 0
for i in range(N):
    minNum = 1001
    for j in range(len(arr)):
        if minNum > arr[j] and preNum < arr[j]:
            minNum = arr[j]
    preNum = minNum
    print(minNum)
    
'''
for i in range(N):
    minNum = 1001
    for j in range(len(arr)):
        if minNum > arr[j]:
            minNum = arr[j]
    arr.remove(minNum)
    print(minNum)
'''