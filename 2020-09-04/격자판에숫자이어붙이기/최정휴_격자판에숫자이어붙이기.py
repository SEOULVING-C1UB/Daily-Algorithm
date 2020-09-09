'''
<기본컨셉>
1) 주어진 4X4행렬의 모든 원소를 방문하며 이를 시작점으로 꼬리물기를 시작한다
2) 현재 위치를 기반으로 상하좌우를 방문하여 꼬리를 물며 이어 붙이는 재귀함수를 만든다
3) 만들어진 문자열을 리스트에 담은 후 set을 이용해 중복을 제거한다

<주의사항>
1) 상하좌우를 돌릴때 음수 인덱스는 에러가 안나므로 꼭 try가 아닌 if문으로 0에서 n까지 조건 처리할것
2) 꼬리물기하는 결과를 재귀함수안에서 리스트로 처리하면 역시나 문제가된다
'''

def makeworm(x,y,n,worm):                           # 숫자이어붙여진게 지렁이 같아서 makeworm으로 이름 붙임
    if n == 6:                                      # 6번의 시행후 만들어진 문자열을 worms리스트에 append
        worms.append(worm)
    else:
        for i in range(4):                          # 상하좌우에 대하여
            if 0<=x+dx[i]<4 and 0<=y+dy[i]<4:       # 인덱스 범위를 만족하면 좌표 변경 및 문자열 추가
                makeworm(x+dx[i], y+dy[i], n+1, worm+field[y+dy[i]][x+dx[i]])


t = int(input())
for i in range(1,t+1):
    field = [list(input().split()) for _ in range(4)]
    worms = []
    dx = [1, -1, 0, 0]                              # 상하좌우 델타검색용
    dy = [0, 0, 1, -1]
    for y in range(4):                              # 모든 점을 시작점으로 돌아야 하므로 이중 반복문 작성
        for x in range(4):
            makeworm(x, y, 0, field[y][x])
    print('#{} {}'.format(i,len(set(worms))))