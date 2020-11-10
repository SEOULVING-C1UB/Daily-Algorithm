'''
<문제해결>
 : 이전에 풀었던 창용마을 무리의 갯수와 아주 유사한 문제이다. bfs이용
1) 현재 사람으로 부터 연결된 모든 사람들을 확인
2) 연결된 사람들로부터 다시 연결된 사람들을 반복 확인하여 무리를 파악
3) 방문표시를 통해 선택된 사람 재방문 제거
'''

import sys
sys.stdin = open("5248_그룹나누기.txt")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    field = [[0]*(n+1) for _ in range(n+1)]     # 연결관계를 표시할 리스트
    visited = [0]*(n+1)                         # 방문표시
    lst = list(map(int, input().split()))
    groups = []                                 # 그룹들을 저장할 리스트
    for i in range(m):                          # 연결관계 저장
        field[lst[i*2]][lst[i*2+1]] = field[lst[i*2+1]][lst[i*2]] = 1

    for j in range(1,n+1):                      # 모든 사람들에 대해 반복문
        if visited[j] != 1:                     # 방문한적이 없으면
            visited[j] = 1                      # 방문표시
            group = [j]                         # 현재 사람을 기준으로 그룹 생성
            now = [j]                           # 현재 연결관계 확인용
            new = []                            # 새로 연결된사람들 넣는용도
            while len(now) != 0:                # 더이상 확인할 사람이 없을때 까지
                for k in now:                   # now에 있는 사람들에 대해
                    for l in range(1,n+1):      # 연결된사람이 있으면
                        if field[k][l] == 1 and visited[l] == 0:
                            visited[l] = 1      # 방문표시하고
                            new.append(l)       # 새로연결된 사람에 추가
                            group.append(l)     # 그룹에도 추가
                now = new                       # now의 모든사람을 확인후 새로추가된 사람들을 now로 대체
                new = []                        # new는 초기화
            groups.append(group)                # 더이상 추가할 사람이 없으면 그룹들에 그룹 추가
    print('#{} {}'.format(tc,len(groups)))