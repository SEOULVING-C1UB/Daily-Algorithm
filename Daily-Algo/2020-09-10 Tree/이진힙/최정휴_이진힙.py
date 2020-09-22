import sys
sys.stdin = open("5177_이진힙.txt")

'''
<풀이과정>
: 최소힙
1) 현재 노드의 위치에 주어진 값을 입력
2) 부모 노드와 비교하여 부모 노드가 크면 swap
3) 이 과정을 반복
'''

def minheap(num):
    global cnt                              # 전역 변수 설정
    cnt += 1                                # 인덱스 1 증가
    nodes[cnt] = num                        # 현재노드에 값 저장
    child = cnt                             # 현재노드를 자식노드로 
    parrent = child//2                      # 현재노드의 부모노드

    while parrent != 0 :                    # 루트에 도달하기 전 까지
        if nodes[parrent] > nodes[child]:   # 부모 노드값이 더 크면 swap
            nodes[parrent], nodes[child] = nodes[child],  nodes[parrent]
            child = parrent                 # swap후 부모노드를 자식노드로
            parrent = child//2
        else:                               # 부모가 더 작으면 리턴
            return

t = int(input())

for i in range(1,t+1):
    n = int(input())
    nodes = [0]*(n+1)
    nums = list(map(int,input().split()))
    cnt = 0
    for num in nums:
        minheap(num)
    ans = 0
    while cnt != 0:
        cnt //= 2
        ans += nodes[cnt]
    print('#{} {}'.format(i, ans))