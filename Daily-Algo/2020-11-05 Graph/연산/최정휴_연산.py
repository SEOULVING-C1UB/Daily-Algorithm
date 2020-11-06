'''
<문제해결>
 : bfs로 가능한 모든 경우 탐색하여 정답 도출
1) 연산대상이 되는 숫자에 +1, -1, *2, -10을 연산하여 리스트에 담는다
2) 이때 중복 계산을 방지하기 위해 숫자들의 방문표시 리스트를 만든다.
3) 그렇게 만들어진 모든 결과를 리스트에 담고 해당 리스트의 숫자를 대상으로 다시 연산을 반복한다.
4) 반복문이 시작할 때 마다 ans를 1 증가시켜 현재 depth확인
4) 목표 숫자인 m이 리스트에 있으면 ans가 정답
<추가사항>
1) 방문표시 안하거나 숫자 크기 판단 안하면 안된다 ㅜㅜ
2) 방문처리 하고나면 중복 없으니까 list(set(new)) 안해도 될거같은데 왜 뺴면 더 느리지ㅜㅜ
'''


import sys
sys.stdin = open("5247_연산.txt")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    ans = 0                                 # 정답 초기화
    visited = [0]*1000001                   # 방문처리 리스트
    lst = [n]                               # 반복문의 대상이 될 리스트. 시작 값인 n을 넣어둔다
    visited[n] = 1                          # n 방문 표시
    while True:
        new = []                            # lst를 교체할 빈 리스트 
        ans += 1                            # 반목문 시작할 때 depth 1증가
        for num in lst:                     # lst에 들어있는 숫자들에 대해 4가지연산 수행
            now = num + 1                   # 각 연산에 대해 결과값이 범위 안에 들고 방문한 적이 없으면 new에 추가
            if 0 < now <= 1000000 and visited[now] == 0:
                new.append(now)
                visited[now] = 1
            now = num - 1
            if 0 < now <= 1000000 and visited[now] == 0:
                new.append(now)
                visited[now] = 1
            now = num * 2
            if 0 < now <= 1000000 and visited[now] == 0:
                new.append(now)
                visited[now] = 1
            now = num - 10
            if 0 < now <= 1000000 and visited[now] == 0:
                new.append(now)
                visited[now] = 1
        lst = list(set(new))                # 네가지의 연산이 끝난 후 new의 중복을 제거하고 lst를 교체.
        new = []                            # new 초기화
        if m in lst:                        # m이 발견되면 break
            break
    print(f'#{tc} {ans}')