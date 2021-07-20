N = input()
length = len(N)

n1 = N[:length//2]
n2 = N[length//2:]

n1_tot = 0
n2_tot = 0
for i in range(length//2):
    n1_tot += int(n1[i])
    n2_tot += int(n2[i])

if n1_tot == n2_tot:
    print("LUCKY")
else:
    print("READY")