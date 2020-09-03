'''
<기본컨셉>
1) 재귀호출을 이용하여 합을 증가시켜가며 선택한다.
2) 이전에 사용한 인덱스를 idx에 저장하여 피하며 진행한다.
3) 백트래킹을 사용해 최소합을 넘는경우 가지치기 한다.

<주의사항>
1) 처음에 idx를 리스트로 만들었었는데 이럴경우 idx가 값형이 아니기 때문에 이전단계의 idx도 변형된다.
2) 이거 고쳐보려고 엄청 해보다가 계속 실패해서 그냥 idx를 문자열로 넣었는데 9월2일 수업에서 교수님 방법으로 해결하면 되더라
'''

import sys
sys.stdin = open("4881_배열최소합.txt")

def ssum(lst, n, N, idx, s):
    global min_sum                                              # 최소합 전역변수로 사용
    if s >= min_sum:                                            # 현재합이 최소합을 넘을경우 가지치기
        return
    if n == N :                                                 # 깊이가 N에 도달한경우
        if s < min_sum:                                         # 최소합과 비교하여 작으면 최소합에 저장
            min_sum = s
    else:
        for i in range(N):
            if str(i) not in idx:                               # 방문한 인덱스가 저장된 idx에 현재 인덱스가 없는경우
                ssum(lst, n+1, N, idx+str(i), s+lst[n][i])      # n은 1증가, idx에 현재 인덱스 추가하고 현재합에 현재 값을 더하여 재귀호출

t = int(input())

for i in range(1, t+1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 1000000000                                        # 최소합의 초기값은 충분히 크게 설정
    ssum(nums, 0, N, "",0)
    print('#{} {}'.format(i, min_sum))