# 주석은 내일 달께요!!

# 망한 코드
# def color(lst, n, N, s, now):
#     global min_s
#     if s >= min_s:
#         return
#     if n == 0:
#         color(lst, n+1, N, s+(M-lst[0][0]), now)
#     elif n == N-1:
#         color(lst, n+1, N, s+(M-lst[n][2]), now)
#     elif n == N:
#         if s < min_s:
#             min_s = s
#     else:
#         for i in range(now, now+2):
#             try:
#                 color(lst, n+1, N, s+(M-lst[0][i]), i)
#             except:
#                 return


t = int(input())

for i in range(1, t+1):
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    flag_cnt = [[f.count("W"), f.count("B"), f.count("R")] for f in flag]
    min_s = 10000000
    # color(flag_cnt, 0, N, 0, 0)
    
    for j in range(1,N-1):
        for k in range(j, N-1):
            s = 0
            for l in range(N):
                if s >= min_s:
                    break
                if l < j:
                    s += M-flag_cnt[l][0]
                elif l > k:
                    s += M-flag_cnt[l][2]
                else:
                    s += M-flag_cnt[l][1]
            if s < min_s:
                min_s = s
    print('#{} {}'.format(i, min_s))
