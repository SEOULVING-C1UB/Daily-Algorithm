'''
[컨셉]
1) dfs를 통해 이어진 주민들의 visited에 동일한 숫자를 넣어줌 (해당 코드에서는 group)
'''

def dfs(start) :                        # dfs 알고리즘
    global group
    s = []
    s.append(start)
    visited[start] = group              # 다른 점은 visited에 몇번째 group인지를 저장
    while s :
        v = s.pop()
        for w in li[v] :
            if not visited[w] :
                visited[w] = group
                s.append(w)
    group +=1                           # 하나의 그룹 찾기가 완료되면 +1
    

T = int(input())
for t in range(T) :
    N, M = map(int, input().split())
    li = [0] + [[] for _ in range(N)]   # 입력은 인접 리스트로 받기
    for edge in range(M):               # 서로 아는 사이니까, 양쪽에 추가.
        s, e = map(int, input().split())    
        li[s].append(e)
        li[e].append(s)
    visited = [0] * (N+1)               # 방문표시를 할 list.
    group = 1                           # 몇번째 group인지 표시할 변수 
    k = 1                               # 어떤 사람에서부터 dfs를 시작할지 담을 변수
    while visited.count(0) > 1 :        # 0번 사람이 있어서, 그를 제외한 모든 이가 방문될 동안
        dfs(k)                          # k번 사람에서 시작해 dfs
        for i in range(k+1, N+1) :      # 그 다음 사람부터 확인해서
            if not visited[i] :         # 방문된 적 없는 사람을 찾아
                k = i                   # k에 넣어줌
                break
    print('#{} {}' .format(t+1, group-1))   # group-1인 이유는, 마지막에 dfs에서 +1했는데, 새 그룹을 찾지는 못하고 반환되기에
