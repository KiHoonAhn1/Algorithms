'''
순열
visited 를 사용하지 않으면 중복순열
'''
def perm(idx): # idx : 선택한 원소가 들어갈 자리(sel)
    global visited, sel
    if N == idx:
        print(sel)
        return
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            sel[idx] = arr[i] # arr[i] 원소를 선택해서 idx 번째에 위치함
            perm(idx+1)
            visited[i] = 0


arr = [1, 2, 3]     # 순열을 만들기 위한 원소
N = len(arr)        # 순열의 길이
sel = [0] * N       # 만들어진 순열 저장  -> 1, 2, 3 / 1, 3, 2 ...
visited = [0] * N   # 선택 여부 저장     -> 0, 0, 1
perm(0)