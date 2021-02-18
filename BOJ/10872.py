def factorial(N):
    if N <= 1:
        return 1
    else:
        N -= 1
        return N * factorial(N)

N = int(input())
print(factorial(N))