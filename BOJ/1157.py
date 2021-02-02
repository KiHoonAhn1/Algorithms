A = input().upper()
B = set(A.upper())

maxA = 0
countList = []
for i in B:
    countList.append(A.count(i))
    if maxA < A.count(i):
        maxA = A.count(i)
if countList.count(maxA) != 1:
    print('?')
elif countList.count(maxA) == 1:
    for j in B:
        if maxA == A.count(j):
            print(j)