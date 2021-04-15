arr = [1, 2, 3]

N = 3

sel = [0] * N
check = [0] * N

def perm(idx):
    # 다 뽑아서 정리했다면
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i] # 값을 써라
                check[i] = 1 # 사용을 했다는 표시
                perm(idx+1)
                check[i] = 0

perm(0)