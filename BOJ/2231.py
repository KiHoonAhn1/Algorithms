N = input()
non = True
for i in range(int(N)):
    tot = i
    for j in str(i):
        tot += int(j)
    if tot == int(N):
        non = False
        print(i)
        break
if non:
    print(0)