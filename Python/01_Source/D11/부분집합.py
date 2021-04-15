'''
1,2,3,4,5,6,7,8,9,10 의 powerset 중 원소의 합이 10인 부분집합을 구하시오
'''

def f(i, N, K):        # i : idx
    global dist
    if i == N: # bit의 모든 칸이 결정됨
        # print(bit, end=' ')
        s = 0
        for j in range(N):
            if bit[j] == 1:
                s += j+1
        if s == K:
            for k in range(N):
                if bit[k] : print(k+1, end=' ')
            print()
            dist += 1
        return
    else:
        bit[i] = 0
        f(i+1,N,K)
        bit[i] = 1
        f(i+1,N,K)


N = 10 # 1부터 N까지 : 집합의 원소
K = 10 # 부분집합의 합 : 10
dist = 0
bit = [0] * N # 해당 원소의 선택여부를 저장
f(0,N,K)