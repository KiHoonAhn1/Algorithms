import sys

N = sys.stdin.readline().rstrip()
arr = []
stack = []
for i in N:
    if i == '-':
        if stack:
            arr.append(')')
            stack.pop()
            arr.append(i)
            stack.append('(')
            arr.append('(')
            continue
        else:
            arr.append(i)
            arr.append('(')
            stack.append('(')
            continue
    arr.append(i)
if stack:
    arr.append(')')
X = len(arr)
number = []
for j in range(X):
    if arr[j-1] == '(' and arr[j] == ')':
        continue
    if arr[j-1] == '+' or arr[j-1] == '-' or arr[j-1] == '(' or arr[j-1] == ')':
        if arr[j] == '0':
            continue
        else:
            number.append(arr[j])
    else:
        number.append(arr[j])
print(number)
print(eval(''.join(number)))