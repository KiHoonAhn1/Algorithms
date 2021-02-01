A = input()
AList = []
for a in range(ord('a'), ord('z')+1):
    AList.append(str(A.find(chr(a))))
print(' '.join(AList))