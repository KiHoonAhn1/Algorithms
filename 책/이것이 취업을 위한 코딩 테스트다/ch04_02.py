N = int(input())
h, m, s = 0, 0, 0
cnt = 0
while h <= N:
    if '3' in str(h) or '3' in str(m) or '3' in str(s):
        cnt += 1
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0

print(cnt)