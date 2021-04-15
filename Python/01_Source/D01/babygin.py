num = 456789
c = [0]*12

for i in range(6):
    A = num % 10
    c[A] += 1
    num //= 10
print(c)

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
    i += 1

if tri + run == 2:
    print('babygin')
else:
    print('fail')