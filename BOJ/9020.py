def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

primeList = prime_list(10002)
T = int(input())
for tc in range(T):
    N = int(input())
    a = N//2
    b = a
    while a>0:
        if a in primeList and b in primeList:
            print(a, b)
            break
        else:
            a-=1
            b+=1