import sys
sys.stdin = open('컨테이너 운반.txt')

T = int(input())

for tc in range(1,1+T):
    n,m = map(int,input().split())

    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    container.sort()
    truck.sort()
    visited = [0]*len(container)

    goal = 0

    for q in range(1,len(truck)+1):
        goal_max = 0 # 0을 못옮기면 0을 출력해야 하므로 for문 안에 집어넣어서 계속 초기화 시켜줌
        for w in range(1,len(container)+1):
            if container[-w] <= truck[-q] and visited[-w] == 0: # 최대값을 구하기 위해 적재용량이 가장 큰 트럭이 적재 가능한 최대 무게의 컨테이너를 운반하기 위해 뒤에서부터 검색
                visited[-w] = 1 # 중복 방지를 위한 체크
                goal_max = container[-w]
                goal += goal_max
                break
    print('#{} {}'.format(tc,goal))