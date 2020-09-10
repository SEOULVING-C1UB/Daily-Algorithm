'''
[컨셉]
1) 입력 받아서 순회하며 몇개 순회했는지 저장
   - postorder traversal 써봤음
'''

import sys
sys.stdin = open("(5174)subtree_input.txt")


def postorder(k):
    global cnt                  # cnt를 증가할 것이니 global로
    if k <= V :                 # 범위 내에 있는 동안
        if len(T[k]) > 0:       # 왼쪽 자식이 있다면 순회
            postorder(T[k][0])
        if len(T[k]) > 1:       # 오른쪽 자식이 있다면 순회
            postorder(T[k][1])
        cnt += 1                # 현 노드에서 + 1


TC = int(input())
for tc in range(TC):
    # 입력 받기
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))

    # 트리에 저장하기
    V = E + 1                                   # V : 노드 몇개인지
    T = [[] for _ in range(V + 1)]
    for e in range(E):
        T[temp[2 * e]].append(temp[2 * e + 1])

    # 순회하며 개수 세기
    cnt = 0                                     # 몇 개의 노드를 방문했는지 저장
    postorder(N)                                # 후위 순회
    print('#{} {}'.format(tc + 1, cnt))
