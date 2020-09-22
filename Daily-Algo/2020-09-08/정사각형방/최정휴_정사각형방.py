'''
<기본컨셉>
 : bfs를 이용 델타검색을 하여문제를 해결한다.
 1) NxN의 모든 정점을 시작점으로 하여 상하좌우 델타검색을 한다.
 2) 상하좌우에 1큰 값이 있으면 옮겨가서 재귀호출
 3) 현재 합이 최댓값보다 크면 처음 시작점과 합의 값을 갱신
 4) 현재 합이 최댓값과 같으면 처음시작점을 비교해 더 작은경우 갱신

 <추가사항>
 1) 시간초과는 아니지만 짱오래걸린다.. 속도 빠르게 해결할 방법을 찾아보자
'''

def search(s, x, y, S):
    global max_S                                # 전역변수 설정
    global start
    if S > max_S or (S == max_S and s < start): # 최댓값과 시작점 갱신 여부 확인
        max_S = S
        start = s
    for i in range(4):                          # 네 방향 델타검색
        if 0<=x+dx[i]<N and 0<=y+dy[i]<N and (field[y][x] - field[y+dy[i]][x+dx[i]] == -1):
            search(s, x+dx[i], y+dy[i], S+1)    # 재귀호출
            
t = int(input())

for i in range(1,t+1):
    N = int(input())
    field = [list(map(int,input().split())) for _ in range(N)]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    max_S = 0
    start = 1000000
    for x in range(N):                          # NxN모든 정점에서 시작
        for y in range(N):
            search(field[y][x], x, y, 1)
    print('#{} {} {}'.format(i, start, max_S))