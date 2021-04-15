import math
arr = [ 0,0,0,0,0,0,0,1,1,1, 1,0,0,0,0,0,0,1,1,0, 0,0,0,0,0,1,1,1,1,0, 0,1,1,0,0,0,0,1,1,0, 0,0,0,1,1,1,1,0,0,1, 1,1,1,0,0,1,1,1,1,1, 1,0,0,1,1,0,0,1,1,1]
answer = [0 for _ in range(math.ceil(len(arr)/7))]
for i in range(math.ceil(len(arr)//7)):
    result = 0
    for j in range(7):
        result += arr[7*i + j] * (1<<(6-j))
    answer[i] = result

print(answer)