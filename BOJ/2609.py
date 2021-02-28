A, B = map(int, input().split())
A_arr, B_arr = [], []
for i in range(1, A+1):
    if not A % i:
        A_arr.append(i)

for j in range(1, B+1):
    if not B % j:
        B_arr.append(j)

# 안되면 거꾸로 하고 바로 break
max_ab = 0
for a in A_arr:
    for b in B_arr:
        if a == b and max_ab < a:
            max_ab = a

print(max_ab, int(B/max_ab*A))
