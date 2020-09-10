'''
[컨셉]
1) minheap을 만들어서 삽입 연산 수행
2) 마지막 노드의 부모부터 시작해서, 루트 노드에 도달할 때까지 계속 그 부모를 거슬러 올라가며 값 더하기
'''

import sys
sys.stdin = open("(5177)이진 힙_input.txt")


def heappush(k):                                # 최소힙에 삽입하는 연산
    miniheap[cnt] = k                           # 일단 현재 시점에서 맨 끝에 값을 넣어두고
    cur = cnt                                   # cur : 현재 노드 번호
    parent = cur // 2                           # parent : 현재 노드의 부모
    while parent > 0:                           # 부모가 루트 노드일 때까지
        if miniheap[parent] > miniheap[cur]:    # (부모의 값) > (자식의 값)이라면 swap 
            miniheap[parent], miniheap[cur] = miniheap[cur], miniheap[parent]
            cur = parent                        # 현재의 위치를 부모로 옮기고
            parent = cur // 2                   # 변경된 현재 위치의 부모 노드 저장
        else:                                   # 만약 변경이 필요없다면, 제자리 도착.
            break


TC = int(input())
for tc in range(TC):
    # 입력
    N = int(input())
    numbers = list(map(int, input().split()))
    
    # minheap 구성
    miniheap = [0] * (N + 1)
    cnt = 0
    for num in numbers:
        cnt += 1
        heappush(num)

    # 부모 노드들의 값 더하기
    till = N // 2                   # 마지막 노드의 부모 노드
    result = 0                      # 더한 값 저장
    while till > 0:                 # 루트 노드에 갈 때까지
        result += miniheap[till]    # 값을 더하고
        till //= 2                  # 현재 노드의 부모로 바꿔주기
    print('#{} {}'.format(tc + 1, result))
