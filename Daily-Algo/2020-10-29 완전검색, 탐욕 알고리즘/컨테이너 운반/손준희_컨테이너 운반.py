for TC in range(int(input())):
    N, M = map(int, input().split())
    goods = list(map(int, input().split()))     # 물건들 무게 리스트
    trucks = list(map(int, input().split()))    # 트럭들 적재량 리스트
    trucks.sort()
    trucks.reverse()    # 내림차순 정렬
    goods.sort()
    goods.reverse()     # 내림차순 정렬
    weight = 0  # 총 옮긴 무게
    for i in range(M):                  # 적재량이 큰 트럭부터 순서대로
        for j in range(N):              # 무게가 무거운 물건들부터 순서대로
            if trucks[i] >= goods[j]:   # 트럭 적재 수용량이 물건 무게보다 크면
                weight += goods[j]      # 옮긴 무게에 계산한다.
                goods[j] = 999999       # visit 체크 대신으로 해당 물건을 아주 무겁게 바꾼다.
                break                   # 트럭 1대당 물건 1개이므로 break 한다.
    print('#{} {}'.format(TC + 1, weight))



    # while trucks and goods:
    #     truck = trucks.pop()
    #     good = goods.pop()
    #     while good > truck and goods:
    #         good = goods.pop()
    #     weight += good
    # print('#{} {}' .format(TC+1, weight))
