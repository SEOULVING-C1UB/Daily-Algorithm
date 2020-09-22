'''
<해결방법>
 : dfs와 인접리스트를 이용. 노드의 부모 갯수를 파악하며 진행한다.
1) 우선 각 노드의 부모를 담은 리스트와 자식을 담은 리스트를 만든다.
2) 각 노드를 순회하며 부모가 없는 노드를 시작점으로 출발한다. 이때 작업 순서에 현재 노드를 추가한다.
3) 현재 노드는 자식 노드에 대해 부모 노드이므로 자식노드의 부모 노드에서 현재노드를 삭제함으로써 방문 처리를 한다.
4) 자식 노드에 대해 재귀 호출을 사용하는데 이때 부모가 현재 노드 밖에 없었다면 삭제과정에서 남은 부모 노드가 없으므로 진행이될것이고
5) 만약 남아있는 부모 노드가 있다면 진행이 되지 않고 나머지 순회가 돌아간다.
6) 끝까지 진행되면 workflow를 출력한다.

<추가사항>
1) 만약 사이클릭한 경우가 존재하면 아주 골치아플것이다.
2) 리스트 반복문 없이 출력하려고 join써봤는데 리스트안에 문자열이어야 작동하더라
'''

def work(s):
    if len(parents[s]) == 0:                # 부모 노드가 없으면
        workflow.append(s)                  # 작업순서에 추가
        for child in childs[s]:             # 현재노드의 자식 노드들에 대해
            parents[child].remove(s)        # 자식노드의 부모노드에서 현재노드 삭제
            work(child)                     # 자식노드에 대해 재귀호출

for i in range(1, 11):
    V, E = map(int, input().split())
    lst = list(map(int, input().split()))
    parents = [[] for _ in range(V+1)]      
    childs = [[] for _ in range(V+1)]       
    workflow = []
    for j in range(E):
        parents[lst[2*j+1]].append(lst[2*j])# 부모노드 리스트 생성
        childs[lst[2*j]].append(lst[2*j+1]) # 자식노드 리스트 생성
    for j in range(1,V+1):
        if j not in workflow:               # 작업순서에 반영되지 않은 노드에 대해 함수 실행
            work(j)
    print(f"#{i}", end=" ")
    for w in workflow:
        print(w, end=" ")
    print()