def merge(left, right):
    result = []
    # i, j 사용하지 않고 pop하면 시간초과
    i = 0
    j = 0
    while len(left) > i or len(right) > j:
        if len(left) > i and len(right) > j:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif len(left) > i:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result

def merge_sort(arr):
    global cnt

    if len(arr) == 1:
        return arr

    m = len(arr)//2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)
    print(f'#{tc} {arr[N//2]} {cnt}')
