def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, c)
        hanoi(n - 1, b, a, c)
        
T = int(input())
total = 0
for i in range(T):
    total = total * 2 + 1

print(total)
hanoi(T, 1, 2, 3)
