arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def backtrack(c_arr, i):
    if sum(c_arr) == 10:
        print(c_arr)
        return
    elif sum(c_arr) > 10:
        return

    if i >= length:
        return
    c_arr.append(arr[i])
    backtrack(c_arr, i+1)
    c_arr.pop()
    backtrack(c_arr, i+1)

length = len(arr)
backtrack([], 0)