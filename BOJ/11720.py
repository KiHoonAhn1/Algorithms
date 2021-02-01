N = int(input())
A = input()
total = 0
if N == len(A):
    for i in A:
        total += int(i)
print(total)