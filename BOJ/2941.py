croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
C = input()
count = 0
for i in croatia:
    if i in C:
        count += C.count(i)
        C = C.replace(i, '*', C.count(i))
C = C.replace('*', '')
count += len(C)
print(count)