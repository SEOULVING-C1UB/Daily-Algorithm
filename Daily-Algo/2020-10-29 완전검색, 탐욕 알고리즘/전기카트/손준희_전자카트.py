def find_permu():
    if now_cost[0] > min_cost[0]:   # 가지치기 부분
        return
    if len(ptn) == N:                                       # 순열아 만들어지면
        if min_cost[0] > now_cost[0] + table[ptn[-1]][0]:   # 총 배터리 소모량을 최소 배터리 소모량과 비교해서
            min_cost[0] = now_cost[0] + table[ptn[-1]][0]   # 최소 배터리 소모량을 갱신한다.
        return
    for i in range(1, N):
        if not check[i]:                            # 방문 안 한 경우에
            check[i] = 1                            # 방문했다고 치고
            ptn.append(i)                           # 순열 뒤에 붙이고
            now_cost[0] += table[ptn[-2]][ptn[-1]]  # 현재 배터리 소모량에 배터리 소모값을 추가한다.
            find_permu()                            # 그리고 재귀한다.
            now_cost[0] -= table[ptn[-2]][ptn[-1]]  # 현재 배터리 소모량에 바로 직전에 추가했던 배터리 소모값을 빼준다.
            ptn.pop()                               # 그리고 뒤에 붙였던거 떼내고
            check[i] = 0                            # 방문 안 했다고 친다.


for TC in range(int(input())):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(N)]
    check = [0 for i in range(N)]
    ptn = [0]   # 출발지는 1번(index = 0)이므로 넣고 시작한다.
    min_cost = [99999]  # global 없이 접근하기 위함
    for i in range(1, N):           # 2번(index = 1)부터 N번(index = N-1)에서 각각 시작하는 경우 고려하기
        now_cost = [table[0][i]]    # 마찬가지로 global 없이 접근하기 위함
        check[i] = 1                # i+1번 구역을 방문했다고 체크하고
        ptn.append(i)               # 순열 ptn 뒤에 붙인다
        find_permu()                # 순열찾기 함수를 실행하고
        check[i] = 0                # 방문체크 해제하고
        ptn.pop()                   # 뒤에 붙였던거 뗀다.
    print('#{} {}' .format(TC+1, min_cost[0]))



# def find_permu():
#     if len(ptn) == N-1:
#         if [0] + ptn + [0] not in routes:
#             routes.append([0] + ptn + [0])
#             return
#     for i in range(1, N):
#         if not check[i]:
#             check[i] = 1
#             ptn.append(i)
#             find_permu()
#             check[i] = 0
#             ptn.pop()
#
#
# for TC in range(int(input())):
#     N = int(input())
#     table = [list(map(int, input().split())) for i in range(N)]
#     check = [0 for i in range(N)]
#     check[0] = 1
#     ptn = []
#     routes = []
#     for i in range(1, N):
#         check[i] = 1
#         ptn.append(i)
#         find_permu()
#         check[i] = 0
#         ptn.pop()
#     min_cost = 999999
#     for route in routes:
#         now_cost = 0
#         for idx in range(N):
#             if now_cost > min_cost:
#                 break
#             now_cost += table[route[idx]][route[idx+1]]
#         if min_cost > now_cost:
#             min_cost = now_cost
#     print('#{} {}' .format(TC+1, min_cost))