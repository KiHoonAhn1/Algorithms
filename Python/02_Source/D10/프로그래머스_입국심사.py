# 프로그래머스에서는 times array를 전달해줘야 인식함
def immigration(l, r, n, times):
    global answer
    if l > r:
        return

    m = (l + r) // 2
    total = 0
    for time in times:
        total += m // time
    if n > total:
        immigration(m+1, r, n, times)
    elif n <= total:
        answer = m
        immigration(l, m-1, n, times)

# 둘 다 answer을 global로
def solution(n, times):
    global answer
    l = 0
    r = 1000000000 * 1000000000
    immigration(l, r, n, times)
    return answer