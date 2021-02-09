def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

while True:
    N = int(input())
    if N == 0:
        break
    count = 0
    for j in prime_list(2 * N + 1):
        if j > N:
            count += 1
    print(count)
