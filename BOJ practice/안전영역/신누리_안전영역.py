'''
[컨셉]
1) 높이를 입력으로 받아와서, mini와 maxi에 각각 높이의 최소, 최댓값을 저장
2) (비 내리는 양) = (높이의 최소 ~ 최댓값 사이의 수)를 가정해서 가장 많은 영역의 수를 ans에 저장
3) 각 케이스마다 비에 잠기는 영역은 0으로, 그렇지 않은 영역은 1로 표시한 일종의 visited 역할을 하는 sink 사용
4) sink를 토대로 safe 함수를 돌림. safe는 dfs를 하며 안전 영역의 개수를 count
'''

# 컨셉 4
def safe():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if sink[i][j] :
                cnt +=1 
                S = [(i,j)]
                while S :
                    a, b = S.pop()
                    sink[a][b] = 0
                    for k in range(4):
                        if 0<= a + dir1[k] <N and 0<= b+ dir2[k] < N:
                            if sink[a+dir1[k]][b+dir2[k]]:
                                S.append((a+dir1[k], b+dir2[k]))
    return cnt


# 컨셉 1
N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N)]

mini = 101
maxi = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] < mini :
            mini = arr[i][j]
        elif arr[i][j] > maxi :
            maxi = arr[i][j]

dir1 = [1, 0, -1, 0]
dir2 = [0, 1, 0, -1]

# 컨셉 2
ans = 1
for r in range(mini, maxi+1):
    # 컨셉 3
    sink = [ [1]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= r:
                sink[i][j] = 0
    result = safe()
    if result > ans : ans = result

print(ans)
