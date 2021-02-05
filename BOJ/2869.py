A, B, V = map(int, input().split())
day = (V - A) / (A - B)
if day < 1:
    print(int(day)+2)
else:
    print(int(day)+1)