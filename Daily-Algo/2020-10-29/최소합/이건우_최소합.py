import sys
sys.stdin = open('input.txt', 'r')

dx = [1,0]
dy = [0,1]

## 항상 우 또는 하로만 이동할 수 있다. 이동시(dfs 재귀 호출)에 cursum에 해당좌표의 값을 더해준다
## 만약 cursum이 지금까지 구한 최솟값보다 크면 더 나아가지 않고 return 해준다.
## 마지막으로 마지막 지접에 도착하게 되면 최솟값(_min)에 해당 값을 할당한다.



def dfs(s,cursum):
    global _min
    x,y = s
    if cursum > _min:
        return
    if x == y == N-1:
        _min = min(_min,cursum)
        return
    for i in range(2):
        tx,ty = x+dx[i], y+dy[i]
        if tx<N and ty<N:
            dfs([tx,ty], cursum+arr[tx][ty])


for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    _min = 0x7fffffff
    dfs([0,0],arr[0][0])
    print('#{} {}'.format(tc, _min))