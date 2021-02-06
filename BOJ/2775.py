import sys

N = int(sys.stdin.readline())

for x in range(1,int(N)+1):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    people = []
    for x in range(1, n+1):
        people.append(x)
    for y in range(k):
        for z in range(1, n):
            people[z] += people[z-1]
    print(people[-1])