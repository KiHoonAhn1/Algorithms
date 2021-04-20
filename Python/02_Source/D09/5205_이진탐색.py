def binary_search(l, r, key):
    global cnt
    if l > r:
        return

    m = (l + r) // 2
    if A_arr[m] == k:
        cnt += 1
        return
    elif A_arr[m] < k and key != 'right':
        binary_search(m+1, r, 'right')
    elif A_arr[m] > k and key != 'left':
        binary_search(l, m-1, 'left')
    else:
        return

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # A와 B에 속한 정수의 개수
    # 이진탐색은 정렬된 리스트에서만 사용 가능하다.
    A_arr = sorted(list(map(int, input().split()))) # A에 속한 정수의 개수 N
    B_arr = list(map(int, input().split())) # B에 속한 정수의 개수 M

    cnt = 0
    for k in B_arr:
        binary_search(0, N-1, '')
    print(f'#{tc} {cnt}')