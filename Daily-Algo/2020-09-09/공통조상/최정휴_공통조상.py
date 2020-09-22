'''
<문제해결>
1) 각 노드별 자식노드 입력용 리스트와 부모노드 입력용 리스트를 만들어 3차원배열로 정리
 ex) 1 2 1 3의 경우 1번 노드의 자식은 2,3 2번 3번 노드의 부모는 1번이므로
 [[[],[]], [[2,3],[]], [[],[1]], [[],[1]]]과 같이 처리됨
2) 우선적으로 공통 조상을 찾기위해 각각의 조상을 쫓아가며 리스트에 입력후 가장 가까운 조상을 찾아냄
3) 해당 공통조상으로부터의 트리의 크기를 구하는 함수를 만듬
4) 현재노드의 자식노드 갯수를 더하고 자식노드를 재귀호출

<추가사항>
1) 짜놓고도 너무 복잡한데.. 쉽게 다시짜고 싶다..
2) 영어를 못해서 맨날 kuegi이런식으로 짜는데.. 너무 현타온다...
3) 3차원 배열로 만든이유는 왼쪽 자식 오른쪽 자식 확인하기 귀찮아서
'''

def kuegi(v):                                       # 트리의 크기 확인하는 함수
    global cnt                                      # 전역변수 설정
    cnt += len(nodes[v][0])                         # 현재노드의 자식노드 갯수만큼 더하기
    try:                                            # 자식노드가 없어 에러나는 경우는 try문으로 처리
        kuegi(nodes[v][0][0])                       # 자식노드 재귀호출
        kuegi(nodes[v][0][1])
    except:
        return

t = int(input())

for i in range(1,t+1):
    v, e, a, b = map(int,input().split())
    arcs = list(map(int,input().split()))
    nodes = [[[],[]] for _ in range(v+1)]           # 3차원 배열 생성
    j_a = []                                        # a의 조상리스트
    j_b = []                                        # b의 조상리스트
    for j in range(e):
        nodes[arcs[2*j+1]][1].append(arcs[2*j])     # 현재노드의 부모노드 저장
        nodes[arcs[2*j]][0].append(arcs[2*j+1])     # 현재노드의 자식노드 저장
    
    now = nodes[a][1]                               # 현재노드의 부모노드 추적
    while len(now) != 0:                            # 부모노드가 없을때 까지
        j_a.append(now[0])                          # 부모를 a의 조상리스트에 append
        now = nodes[now[0]][1]                      # 현재노드의 부모노드를 현재노드로

    now = nodes[b][1]                               # b에대해 같은 행위를 반복
    while True:
        if now[0] in j_a:                           # 현재 b의 조상이 a의 조상리스트에 있으면
            j_gong = now[0]                         # 가장가까운 공통 조상이므로 공통조상에 저장후 break
            break
        else:
            j_b.append(now[0])
            now = nodes[now[0]][1]
    cnt = 1                                         # 자기 자신도 크기에 포함해야하므로 1로 시작
    kuegi(j_gong)
    print('#{} {} {}'.format(i, j_gong, cnt))