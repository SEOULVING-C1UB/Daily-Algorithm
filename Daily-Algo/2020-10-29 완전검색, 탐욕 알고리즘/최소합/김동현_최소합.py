import sys
sys.stdin = open('최소합.txt')


def my_sum(i,j,res):
    global min_sum # min_sum은 일반 값이기 때문에 수정하기 위해 global 사용
    if res >= min_sum: # 가지치기1
        return

    if i == n-1 and j == n-1: # 탈출 조건, 오른쪽 가장 아래 도착했을 때
        if min_sum > res:
            min_sum = res
        return

    for q in range(2):
        newX = i+x[q]
        newY = j+y[q]

        if newX < n and newY < n: # 범위 조건
            my_sum(newX,newY,res + case[newX][newY])
    return

x = [0,1]
y = [1,0]

T = int(input())

for tc in range(1,1+T):
    n = int(input())
    case = [list(map(int,input().split())) for _ in range(n)]

    min_sum = 10*n # 10 이하의 자연수이기 때문에 n*10 해줌
    
    my_sum(0,0,case[0][0]) # 맨 왼쪽 위이기 때문에 [0][0]이 시작점
    
    print('#{} {}'.format(tc,min_sum))