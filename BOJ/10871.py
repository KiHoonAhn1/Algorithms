N, X = map(int, input().split())
A = input().split()
B = []

for i in range(N):
    if int(A[i]) < X:
        B.append(A[i])

print(" ".join(B))