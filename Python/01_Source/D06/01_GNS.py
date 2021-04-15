T = int(input())
for tc in range(1, T+1):
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    counts = [0 for _ in range(10)]
    A, B = map(str, input().split())
    B = int(B)
    numList = input().split()
    for i in range(len(numList)):
        for j in range(len(nums)):
            if numList[i] == nums[j]:
                counts[j] += 1
                break
    print(A)
    for a in range(len(counts)):
        for b in range(counts[a]):
            print(nums[a], end=' ')
    print()

