'''
<기본컨셉>
1) 맨위에서 부터 흰색 파란색 빨간색이 차례로 등장하기만 하면 된다.
2) 즉, 파란색의 시작점과 끝점을 설정하면 흰색과 빨강색은 자동으로 결정된다.
3) 따라서 파란색의 시작점과 끝점을 이중 반복문을 통해 모두 구현하고
4) 다시 반복문을 이용하여 각행의 비용을 계산한다.

<주의사항>
1) 재귀로 도전했으나 실패.. 파란색이 없는경우를 처리하지 못했다.. 담에 해보자
'''

t = int(input())

for i in range(1, t+1):
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    flag_cnt = [[f.count("W"), f.count("B"), f.count("R")] for f in flag]   # flag리스트를 문자로 두지말고 각 색깔이 몇개인지만 알면 된다.
    min_s = 10000000                                                        # 최솟값 비교 대상은 항상 충분히 크게
    # color(flag_cnt, 0, N, 0, 0)
    
    for j in range(1,N-1):                                                  # 파란색이 들어갈 시작점과 끝점을 이중 반복문으로 구현
        for k in range(j, N-1):
            s = 0
            for l in range(N):                                              # 전체 인덱스에 대해
                if s >= min_s:                                              # 합이 현재 최솟값보다 큰 경우 가지치기
                    break
                if l < j:                                                   # 시작점 이전 : 흰색 부분
                    s += M-flag_cnt[l][0]                                   # 합에다가 M에서 흰색의 갯수를 뺸걸 더한다. 빨강 더하기 파랑을 더해도 상관없다.
                elif l > k:                                                 # 끝점 이후 : 빨강부분
                    s += M-flag_cnt[l][2]                                   # 흰색과 같은 과정
                else:                                                       # 파란부분
                    s += M-flag_cnt[l][1]                                   # 흰색과 같은과정
            if s < min_s:                                                   # 최솟값 갱신
                min_s = s
    print('#{} {}'.format(i, min_s))


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