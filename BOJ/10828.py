import sys

N = int(sys.stdin.readline())
stack = []
for command in range(N):
    command_arr = list(map(str, sys.stdin.readline().split()))
    if command_arr[0] == 'push':
        stack.append(int(command_arr[1]))
    elif command_arr[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif command_arr[0] == 'size':
        print(len(stack))
    elif command_arr[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command_arr[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)