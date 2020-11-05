import sys
sys.stdin = open("화물도크_input.txt")

def scheduler(trucks) :
    global result
    for i in range(len(trucks)) :
        flag = 1
        for j in range(trucks[i][0], trucks[i][1]) :    # 해당 도크의 시작시간부터 끝나는 시간까지
            if visit[j] == 1 :      # 이미 차있는 상태라면
                flag = 0            # flag 0을 바꿔준다.
        if flag :                   # 만약에 flag 가 0으로 안바뀌었으면 -> 빈 상태면
            for k in range(trucks[i][0], trucks[i][1]) :    # 내가 사용가능한 상태니까
                visit[k] = 1        # 방문처리 해주고
            result += 1             # 사용자 수 1 늘려준다.

for tc in range(1, int(input())+1) :

    N = int(input())
    result = 0
    trucks = [list(map(int, input().split())) for _ in range(N)]

    visit = [0] * 25        # 24시간인데 0이 포함되어 25개로 짜준다.

    for i in range(N) :
        trucks[i].append(trucks[i][1]-trucks[i][0])     # 사용 시간을 뒤에 붙여줬다.

    trucks = sorted(trucks, key = lambda x : x [2])     # 사용 시간을 기준으로 정렬했다.
    # 사용시간이 작은것부터 정렬되었는데, 최대한 많은 사용자를 넣으려고 했기 때문이다.
    scheduler(trucks)

    print("#{} {}".format(tc, result))