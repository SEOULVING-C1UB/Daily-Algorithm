import sys
sys.stdin = open('전자키트.txt')


def search(i,res,cnt):
    global min_res
    if res >= min_res: # 가지치기
        return
    if cnt == n: # 탈출조건
        if min_res > res:
            min_res = res
        return

    if cnt == n-1: # 마지막에는 무조건 사무실로 복귀해야 함
        visited[0] = 1
        search(0,res+golf[i][0],cnt+1)
        visited[0] = 0
        return

    if cnt != n-1:
        for q in range(1,n):
            if golf[i][q] != 0 and visited[q] == 0:
                visited[q] = 1
                search(q,res+golf[i][q],cnt+1)
                visited[q] = 0
    return

T = int(input())

for tc in range(1,1+T):
    n = int(input())

    golf = [list(map(int,input().split())) for _ in range(n)]

    visited = [0]*n
    min_res = 100000

    search(0,0,0)

    print('#{} {}'.format(tc,min_res))