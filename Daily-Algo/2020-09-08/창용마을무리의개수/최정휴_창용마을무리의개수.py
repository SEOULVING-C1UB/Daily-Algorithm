'''
<기본컨셉>
1) bfs를 이용하여 문제를 해결한다.
2) 우선 주어진 연결관계를 이용해 입접행렬을 도출하고
3) 1번 사람부터 시작하여 1차적으로 연결된 사람을 모두 찾아 now리스트에 넣는다.
4) 그럼 now리스트의 사람들을 시작으로 반복문을 통해 연결된 모든사람을 다시 찾는다.
5) 이과정을 더이상 연결된 사람이 없을때 까지 반복하여 하나의 무리를 만든다.
6) 방문하지 않은 사람에 대해 해당 과정을 반복한다.

<추가사항>
1) 반복문안에서 리스트를 세개나 돌려가면 써야하는데 더 효율적인 방법은 없을까
2) 무리 수만 가지고 문제를 풀수도 있겠지만 무리가 어떻게 나눠지는지 확인해두면 나중에 쓸모가 있겠지..?
'''

t = int(input())

for i in range(1,t+1):
    N, M = map(int,input().split())
    people = [[0]*(N+1) for _ in range(N+1)]    # 초기 인접행렬
    visited = [0]*(N+1)                         # 방문표시
    mooridle = []                               # 무리들 리스트
    for _ in range(M):
        s, e = map(int,input().split())
        people[s][e] = people[e][s] = 1         # 인접행렬 연결 표시
    for j in range(1,N+1):                      # 모든 사람들에 대해 반복문
        if visited[j] != 1:                     # 방문한적이 없으면
            visited[j] = 1                      # 방문표시
            moori = [j]                         # 무리의 첫번째 사람
            now = [j]                           # 현재 연결관계 확인용
            new = []                            # 새로 연결된사람들 넣는용도
            while len(now) != 0:                # 더이상 확인할 사람이 없을때 까지
                for k in now:                   # now에 있는 사람들에 대해
                    for l in range(1,N+1):      # 연결된사람이 있으면
                        if people[k][l] == 1 and visited[l] == 0:
                            visited[l] = 1      # 방문표시하고
                            new.append(l)       # 새로연결된 사람에 추가
                            moori.append(l)     # 무리에도 추가
                now = new                       # now의 모든사람을 확인후 새로추가된 사람들을 now로 대체
                new = []                        # new는 초기화
            mooridle.append(moori)              # 더이상 추가할 사람이 없으면 무리들에 무리 추가
    print('#{} {}'.format(i,len(mooridle)))