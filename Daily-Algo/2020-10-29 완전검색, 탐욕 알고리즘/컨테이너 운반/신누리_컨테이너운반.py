'''
[컨셉]
1) 화물, 트럭의 적재용량 모두 내림차순으로 정렬한 뒤, 트럭이 와서 가능한 가장 무거운 것을 싣고 가는 방식으로 구현.
'''

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    container.sort(reverse = True)
    truck.sort(reverse=True)
    weight = 0
    for i in range(M):
        cap = truck[i]
        for j in range(N):
            if container[j] and container[j] <= cap:
                weight += container[j]
                container[j] = 0
                break
    print('#{} {}' .format(t+1, weight))
