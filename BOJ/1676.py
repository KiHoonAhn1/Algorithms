N = int(input())
x = 1
for i in range(N-1):
    x *= N
    N -= 1

x = str(x)
print(len(x) - len(x.rstrip('0')))