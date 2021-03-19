N = int(input())
stack = []
arr = [i for i in range(1, N+1)]
arr = arr[::-1]
result = []
is_True = True
for i in range(1, N+1):
    num = int(input())
    if arr:
        while arr[-1] <= num:
            stack.append(arr.pop())
            result.append('+')
            if not arr:
                break
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            is_True = False
    else:
        if stack[-1] == num:
            stack.pop()
            result.append('-')
        else:
            is_True = False
if is_True:
    for i in result:
        print(i)
else:
    print('NO')


