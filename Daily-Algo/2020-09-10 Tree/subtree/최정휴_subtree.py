import sys
sys.stdin = open("5174_subtree.txt")

'''
<풀이과정>
1) 주어진 간선을 이용해서 자식노드를 원소로하는 2차원 배열을 생성한다
2) 해당 노드의 자식노드로 재귀호출을 하는 함수를 만든다
3) 호출을 할때 마다 카운트를 하면 정답
<추가사항>
1) 완전이진트리가 아님에 주의한다
2) 자식이 없는경우를 try문으로 처리한다
'''

def subtree(v):
    global ans                              # 전역변수 설정
    ans += 1                                # 호출시 ans값 1 증가
    try:                                    # 자식이 없어 에러가 나는경우는 try문으로 처리
        subtree(nodes[v][0])
        subtree(nodes[v][1])
    except:
        return

t = int(input())

for i in range(1,t+1):
    e, n = map(int,input().split())
    arcs = list(map(int,input().split()))
    nodes = [[] for _ in range(e+2)]
    for j in range(e):                      # 각 arc를 이용하여 부모 노드에 자식노드 저장
        nodes[arcs[2*j]].append(arcs[2*j+1])
    ans = 0
    subtree(n)
    print('#{} {}'.format(i, ans))