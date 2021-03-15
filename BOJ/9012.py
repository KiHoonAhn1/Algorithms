import sys

N = int(sys.stdin.readline())
for _ in range(N):
    stack = []
    isTrue = True
    brackets = sys.stdin.readline()
    for bracket in brackets:
        if bracket == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                    continue
                elif stack[-1] == ')':
                    print('NO')
                    isTrue = False
                    break
            else:
                print('NO')
                isTrue = False
                break
        elif bracket == '(':
            stack.append(bracket)
    if isTrue and not stack:
        print('YES')
    elif isTrue and stack:
        print('NO')
