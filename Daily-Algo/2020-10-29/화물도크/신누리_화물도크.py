'''
[컨셉]
1) 소요시간이 짧은 순으로 정렬해서, 그 순서대로 원하는 시간이 비어있을 경우 넣는 방식으로 구현.
* 원래 Job scheduling의 탐욕 알고리즘 : 끝나는 시간을 기준으로 정렬해서, 가장 빨리 끝나는 일부터 배치하는 방식
'''

T = int(input())
for t in range(T):
    N = int(input())
    truck = []
    timeline = [1] * 24
    cnt = 0
    for n in range(N):
        s, e = map(int, input().split())
        truck.append([e - s, s, e])
    truck.sort()
    for i in range(N):
        flag = True
        for j in range(truck[i][1], truck[i][2]):
            if not timeline[j]:
                flag = False
                break
        if flag:
            for k in range(truck[i][1], truck[i][2]):
                timeline[k] = 0
            cnt += 1
    print('#{} {}'.format(t + 1, cnt))