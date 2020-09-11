'''
[풀이]
서브트리의 루트 <현재 노드 <오른쪽 서브
= 왼쪽 먼저 처리하고 내꺼 처리한 후 오른쪽 처리
= 중위순회

- 루트에 저장된 값인지 모르고 헤매다가 그냥 단순히 cnt를 해당 루트를 인덱스로 가진 위치에 넣어주면 된다는 것을 깨달음
'''
import sys
sys.stdin = open('이진탐색_input.txt')

def inOrder(n):

    global cnt

    if n > N:
        return

    else:
        inOrder(n*2)
        tmp[n] = cnt
        cnt +=1
        inOrder(n*2+1)

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    tmp = [0] * (N+1)
    cnt = 1

    inOrder(1)

    root = tmp[1]
    ans = tmp[N//2]
    print('#{} {} {}'.format(tc, root, ans))
