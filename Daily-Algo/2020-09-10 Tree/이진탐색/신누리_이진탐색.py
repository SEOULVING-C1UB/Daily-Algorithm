'''
[컨셉]
1) 중위순회를 하면서 cnt를 1씩 증가시켜 넣는 방식
   - 힌트 듣기 전까지는 inorder인지 모르고 BST 구현하려고 헤맸다 :(
'''

import sys
sys.stdin = open("(5176)이진탐색_input.txt")


def inorder(k):
    global cnt                  # 1씩 증가시킬 것이니까 global
    if cnt <= N:                # 1 ~ N의 범위 내에서
        if 2*k > N:             # 만약 자식이 없다면 (리프노드)
            T[k] = cnt          # cnt를 넣어주고 +1
            cnt += 1
        else:
            if 2*k <= N:        # 왼쪽 자식이 있다면 중위순회
                inorder(2*k)    
            T[k] = cnt          # 현재 노드에 cnt 넣어주고 +1
            cnt += 1            
            if 2*k+1 <= N:      # 오른쪽 자식이 있다면 중위순회
                inorder(2*k + 1)


TC = int(input())
for tc in range(TC):
    N = int(input())
    T = [0]*(N+1)
    cnt = 1                     # 1부터 N까지 순서대로 넣어줄 값
    inorder(1)                  # 1번 노드부터 시작
    print('#{} {} {}' .format(tc+1, T[1], T[N//2]))
