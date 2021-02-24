N = input()
arr = []
for i in N:
    arr.append(i)
arr = sorted(arr, reverse=True)
print(''.join(arr))