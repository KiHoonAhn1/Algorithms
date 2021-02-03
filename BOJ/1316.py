N = int(input())
count = 0
for i in range(N):
    A = input()
    check = True
    if len(A) >= 2:
        for j in range(len(A)-1):
            if A[j] != A[j+1]:
                if A[j] in A[j+1:]:
                    check = False
                    break
        if len(set(A)) == 1:
            check = True
    elif len(A) == 1:
        check = True
    if check == True:
        count += 1
print(count)