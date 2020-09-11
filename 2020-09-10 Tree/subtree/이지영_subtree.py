'''
[풀이]
- parent를 인덱스로 했을 때 자식들은 그 인덱스의 값들이라는 것을 알게 됐다.
- 트리 형태: [[0, 0], [6, 0], [1, 5], [0, 0], [0, 0], [3, 0], [4, 0]]
- 따라서 주어진 인덱스의 값들 중 1이상의 값(i)가 있으면 카운트하고 그 i를 인덱스삼아 재귀호출하는 형태로 만듦
'''

import sys
sys.stdin = open("subtree_input.txt")

def findNodes(n):

    global cnt  

    # 만약 자식들이 없으면 그냥 함수 종료
    if tree[n][0] == 0 and tree[n][1] == 0:
        return

    # 자식이 하나라도 있다면 1이상인 자식만 카운트 해줌
    else:
        for i in range(2):
            if tree[n][i] != 0:
                cnt += 1
                findNodes(tree[n][i])
            else:
                findNodes(tree[n][i])


T = int(input())
for tc in range(1, T+1):

    E, N = map(int, input().split())

    # 노드는 1~E+1까지기 때문에 0 ~ E+1까지 만들었다 (0은 비워두면 되니까)
    tree = [[] for _ in range(E+2)]

    nodes = list(map(int, input().split()))

    # tree[부모]에 자식값들은 추가해줌
    for i in range(0, len(nodes), 2):
        parent = nodes[i]
        tree[parent].append(nodes[i+1])

    # 자식이 없는 노드는 빈 리스트를 가지게 되는데, 이걸 어떻게 처리할지 몰라 그냥 0을 다 넣어줬다
    for i in tree:
        if len(i) == 0:     #아예 비었으면 0 두개 넣고
            i.append(0)
            i.append(0)

        elif len(i) == 1:   #하나만 비었으면 그냥 0 한개 넣어줌
            i.append(0)

    cnt = 0
    findNodes(N)
    print('#{} {}'.format(tc, cnt+1))
