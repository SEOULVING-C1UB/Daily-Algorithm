import sys
sys.stdin = open('(5177)이진힙_input.txt','r')

T = int(input())

for t in range(1,T+1):
    N = int(input())
    tmp = list(map(int,input().split()))
    # node의 번호는 완전탐색 트리이므로 오름차순, 1차원 배열의 인덱스와 같음
    # heap의 인덱스 = node, 힙[node] = value 형식으로 값을 할당시킬 것
    heap = [0] * (N+1)

    # i를 1부터 조회하면서 heap node i번째에 와야 할 값에 대해서 매번 정렬하기 위한 함수
    # heap의 i번째 원소는 ~ i-1번째 까지의 노드 값들 중, 부모 노드의 값과 비교하여 가장 작은 것으로 결정함
    def heappush(value,i):
        heapcount = i+1             # 아래의 반복이 i=0부터 시작하므로 heap 인덱스의 시작인 1로 맞춰줍니다.
        heap[heapcount] = value     # 먼저는 heap 배열의 i번째 노드에 value를 할당하고
        cur = heapcount             # 현재와 부모를 비교하는 작업을 반복하기 위해 변수를 설정합니다.
        parent = cur // 2           # 노드의 부모는 항상 짝수나, 홀수나 //2를 통해 구합니다.

        #print(heap,end=" ") # 힙 동작 방식을 알고 싶어서...
        #print(cur, parent)

        # 힙 자료 형의 조건에 부합하도록 삽입한 자료를 정렬하는 과정
        # 앞서 구한 cur의 부모 노드인 parent가 0인지 아닌지 check해주고
        # parent의 값과 cur의 값을 비교하여, 최소힙이므로, 부모 요소가 더 크다면 바꿔줍니다.
        while parent and heap[parent] > heap[cur]:
            heap[parent], heap[cur] = heap[cur], heap[parent]
            # 바꾸고 난 후, 현재 i번째 값을 추가했으므로, 0~i-1까지 부모 요소를 탐색해야 하기 때문에
            # while문에 들어갈 변수를 업데이트 합니다.
            # 바꾸고 난 후 parent 요소를 기준으로 다시 parent의 parent와 비교합니다.
            cur = parent
            parent = cur // 2

            #print(heap,end=" ")    # 힙을 이해하기 위해
            #print(cur,parent)

    # tmp의 길이 N만큼 순회하면서 tmp의 원소를 넣습니다.
    # i는 0부터 시작하므로 i를 1부터 시작하게하고 tmp[i-1]로 바꾸던가
    # heap의 i를 +1 평행 이동 시킬 수 있습니다.
    for i in range(N):
        heappush(tmp[i],i)

    # 합계를 구합니다.
    # 마지막 노드를 last 변수로 가독성을 위해 선언하고
    # last를 2로나눈 값을 parent로 정의하며 parent가 0이 될때까지 값을 더해줍니다.
    total = 0
    last = N
    parent = last//2
    while parent:
        total += heap[parent]
        parent //=2

    print('#{} {}'.format(t,total))