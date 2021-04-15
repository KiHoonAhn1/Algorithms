N = 4
cnt = 0
def recursion(n):
    global cnt
    if n == 1:
        cnt += 1
    else:
        for i in range(n):
            recursion(n-1)

recursion(N)
print(cnt)

