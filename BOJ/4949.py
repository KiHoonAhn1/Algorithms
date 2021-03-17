import sys

while True:
    is_sentence = True
    stack = []
    sentence = sys.stdin.readline()
    if sentence[0] == '.':
        break
    for a in sentence:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    is_sentence = False
            else:
                is_sentence = False
        elif a == '[':
            stack.append(a)
        elif a == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    is_sentence = False
            else:
                is_sentence = False
    if is_sentence and not stack:
        print('yes')
    else:
        print('no')


