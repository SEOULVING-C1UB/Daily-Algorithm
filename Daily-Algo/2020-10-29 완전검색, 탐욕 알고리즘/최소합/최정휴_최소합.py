'''
<문제해결>
 : 재귀를 이용하여 끝점에 도달할 때 까지의 최소합을 구해준다.
1) 시작점에서 끝점으로는 우하향 하기 때문에 현재 시점에서는 오른쪽으로 가거나 아래로 가는것만 가능하다.
2) 맨 아래나 맨 오른쪽에 도착한 경우 더이상 해당 방향으로 진행하지 않는다.
3) 끝점에 도달한 경우 최솟값과 비교하여 작으면 정답을 갱신한다.

<추가사항>
1) 최소합을 구하는 문제이므로 중간에 가지치기를 하면 효율을 더 높일수있겠다. 
'''

import sys
sys.stdin = open("5188_최소합.txt")

def worm(x, y, s):                                  # 최소합을 구할 재귀함수
    global ans                                      # 정답은 전역변수 설정
    if x == n-1 and y == n-1:                       # 끝점에 도달했을 때 갱신여부 확인
        if s < ans:
            ans = s
            return
    elif x == n-1:                                  # 오른쪽 끝에 도달하면 아래로만 재귀 호출
        worm(x, y+1, s+field[y+1][x])
    elif y == n-1:                                  # 아래쪽 끝에 도달하면 오른쪽으로만 재귀 호출
        worm(x+1, y, s+field[y][x+1])
    else:                                           # 오른쪽, 아래로 가는 재귀함수를 각각 호출
        worm(x+1, y, s+field[y][x+1])
        worm(x, y+1, s+field[y+1][x])


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    field = [list(map(int, input().split())) for _ in range(n)]
    ans = 10000000000000                            # 충분히 큰 값으로 설정하여 최솟값 갱신에 문제가 없게
    worm(0, 0, field[0][0])
    print(f'#{tc} {ans}')