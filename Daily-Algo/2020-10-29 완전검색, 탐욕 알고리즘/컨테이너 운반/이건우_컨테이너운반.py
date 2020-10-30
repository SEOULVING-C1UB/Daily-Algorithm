import sys
sys.stdin = open('input.txt', 'r')

## 트럭은 고정이기 때문에 각 트럭에 대해서 모든 컨테이너를 비교, 트럭이 적재할 수 있는 최대 크기의 컨테이너를 새로운 리스트
## move에 저장하는 동시에 해당 컨테이너를 0으로 초기화해준다. 이를 모든 트럭에 대해 반복하는데
## 컨테이너 수가 트럭의 수보다 적을 수도 있기 때문에, container리스트의 합이 0이 되면 자동으로 break를 걸어준다
## 마지막을 move의 합을 구하면 된다.


for tc in range(1,int(input())+1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    move = [0]*M
    for i in range(M):
        _max = 0
        for j in range(N):
            if container[j] <= truck[i]:
                if _max < container[j]:
                    _max = container[j]
                    _maxj = j
        move[i] = _max
        container[_maxj] = 0
        if sum(container) == 0:
            break
    print('#{} {}'.format(tc,sum(move)))