import copy

none_self_num = []
def self(i):
    if i <= 10000:
        a = copy.deepcopy(i)
        for j in str(a):
            a += int(j)
    none_self_num.append(a)
    return self

for i in range(1, 10000):
    self(i)

self_num = []
for i in range(1, 10000):
    if i not in none_self_num:
        print(i)