'''
[컨셉]
1) 트리의 리프 노드에 주어진 값을 저장한다.
2) 재귀함수 findval을 사용해서 1부터 자식 노드의 합을 저장하도록 한다.
   - 왼쪽 자식만 있다면 왼쪽 자식만, 오른쪽 자식도 있다면 왼쪽 + 오른쪽 자식
'''

import sys
sys.stdin = open("(5178)노드의 합_input.txt")

def findval(k):
    if T[k] > 0:                                    # 만약 값이 저장되어 있다면, return
        return T[k]
    else :                                          # 값을 찾아야 한다면
        if 2*k + 1 <= N:                            # 오른쪽 자식이 있을 때
            T[k] = findval(2*k) + findval(2*k + 1)  # 왼쪽 + 오른쪽 계산하여 return
            return T[k]
        else:
            T[k] = findval(2*k)                     # 왼쪽 자식만 있다면, 그걸 담아 return
            return T[k]


TC = int(input())
for tc in range(TC):
    N, M, L = list(map(int, input().split()))
    T = [0] * (N+1)                             # tree
    for m in range(M):                          # leaf node 저장
        idx, val = map(int, input().split())
        T[idx] = val
    findval(1)                                  # 1부터 재귀
    print('#{} {}' .format(tc+1, T[L]))
