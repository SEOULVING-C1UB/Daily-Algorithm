import sys
sys.stdin = open('input.txt', 'r')

## dfs를 이용한다
## 재귀 호출과 동시에 cursum에 배터리 사용량을 더해준다.
## 호출 중간에 cursum이 최솟값 보다 커지면 다음으로 이동하지 않고 return해준다.
## 모든 지점을 방문(sum(visit) == N)해서 처음 위치로 돌아오게 되면 마지막 위치에서 처음 위치로 올 때
## 필요한 배터리 사용량을 마지막으로 더해주고 최솟값인지 판별 후, 최솟값이면  _min에 할당한다.


def dfs(s,visit, cursum):
    global _min
    if cursum > _min:
        return
    if sum(visit) == N:
        cursum += arr[s][0]
        _min = min(cursum,_min)
    for w in range(N):
        if arr[s][w] and not visit[w]:
            visit[w] = 1
            dfs(w,visit, cursum + arr[s][w])
            visit[w] = 0


for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    _min = 0x7fffffff
    visit = [0]*N
    visit[0] = 1
    dfs(0, visit, 0)
    print('#{} {}'.format(tc,_min))