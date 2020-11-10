'''
<문제해결>
 : 종료 시간이 0시에 가까운 것 부터 차례로 넣어 해결
1) 받아온 시간표의 종료시간순으로 정렬
2) 종료시간이 짧은 순으로 해당 시간을 사용체크하고 도크 수 1증가
3) 만약 해당시간에 이미 사용체크가 되어있으면 넘어감
4) 모든 시간표 순회 후 총 도크수가 정답

<추가사항>
1) 모든 조합에 대해 조합에 포함된 도크수가 많은것부터 차례로 검증하여 검증되면 정답을 도출하는 식으로 접근하였으나 시간초과가 뜬다..
2) 그리디하게 접근하는게 답인 경우도 있으나 아닌경우가 더 많으니 이걸 어쩐다.
'''


import sys
sys.stdin = open("5202_화물도크.txt")

# 시간초과나는 코드

# import itertools

# def find():
#     flag = 0
#     for i in range(n):
#         comb = list(itertools.combinations(list(range(n)), n-i))
#         for c in comb:
#             tt = [0 for _ in range(25)]
#             for idx in c:
#                 for check in range(time[idx][0], time[idx][1]):
#                     if tt[check]:
#                         flag = 1
#                         break
#                     else:
#                         tt[check] += 1
#             if flag:
#                 flag = 0
#             else:
#                 print(f'#{tc} {n-i}')
#                 return
        

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    tt = [0 for _ in range(25)]                                 # 각 시간별 사용체크를 할 리스트
    times = [list(map(int,input().split())) for _ in range(n)]
    times = sorted(times, key=lambda x: x[1])                   # 받아오 시간표를 종료시간 기준으로 오름차순정렬
    ans = 0
    for time in times:                                          # 각각의 시간표에 대해
        for i in range(time[0], time[1]):                       # 시작시간부터 종료시간-1 까지 순회
            if tt[i]:                                           # 만약 현재시간이 사용체크 되어있다면 반복문 탈출
                break
            else:                                               # 체크되어있지 않으면 체크
                tt[i] = 1
        else:                                                   # break없이 반복문을 무사히 수행하였으면 도크수 1 증가 
            ans += 1
    print(f'#{tc} {ans}')    
