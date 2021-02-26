# N = int(input())
# cnt_arr = []

# def meeting(s, e, cnt):
#     for i in range(N):
#         if e+1 == s_arr[i]:
#             cnt += 1
#             meeting(s_arr[i], e_arr[i], cnt)
#             cnt_arr.append(cnt)
#             cnt -= 1
#     return cnt_arr


# s_arr, e_arr = [], []
# for _ in range(N):
#     s, e = map(int, input().split())
#     s_arr.append(s)
#     e_arr.append(e)
# for i in range(N):
#     meeting(s_arr[i], e_arr[i], 1)
# print(max(cnt_arr))

N = int(input())