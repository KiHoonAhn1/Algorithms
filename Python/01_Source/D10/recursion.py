def sum2(k):
    if k <= 0:
        return 0
    # else:
        # return k + func(k-1)
    k+sum2(k-1)
print(sum2(10))

def sum(k, total):
    global result
    if k<= 0:
        result = total
        return
    print(k, end=' ')
    sum(k-1, total + k)
result = 0
sum(5, 0)