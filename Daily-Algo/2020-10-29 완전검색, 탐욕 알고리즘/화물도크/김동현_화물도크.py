import sys
sys.stdin = open('화물도크.txt')


T = int(input())

for tc in range(1, 1 + T):
    n = int(input())

    work_table = [list(map(int, input().split())) for _ in range(n)]
    work_table = sorted(work_table,key=lambda x: x[1],reverse=False) # 종료 시간을 기준으로 정렬

    cnt = 0
    index = 0

    for q in range(n):
        if work_table[q][0] >= index:
            index = work_table[q][1] # 종료시간에 가장 근접한 출발 시간을 찾기 위함
            cnt += 1

    print('#{} {}'.format(tc,cnt))