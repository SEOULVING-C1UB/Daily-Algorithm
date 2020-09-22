'''
인접 리스트를 사용한 풀이
1) 최대 가능한 숫자 크기가 100이므로 101의 visit 정보를 반영할 리스트를 생성합니다.
2) enQ BFS 탐색을 통해 visit 할 떄마다 +1의 값을 증가시켜 줍니다.
3) BFS의 결과로 visit 리스트를 반환해주고
4) visit의 배열을 0부터 순회하면서 가장 큰 값을 찾아줍니다.
    4-1) 이 때, 배열의 순회 값이 하나씩 커지므로 크거나 같은 값이라는 조건을 설정하면 됩니다.
'''
for t in range(1,11):
    N, S = map(int,input().split())
    tmp = list(map(int,input().split()))
    node = [[] for _ in range(101)]
    # 노드에 인접 리스트로 반영
    for i in range(N//2):
        fm = tmp[2*i]
        to = tmp[2*i +1]
        node[fm].append(to)
    # enQ BFS 탐색
    def BFS(s):
        # 최대값이 100이므로, 인덱스를 1부터 읽기 위하여
        visit = [0] * 101
        Q = []
        Q.append(s)
        visit[s] = 1
        while len(Q) != 0:
            v = Q.pop(0)
            for w in node[v]:
                if visit[w] == 0:
                    Q.append(w)
                    visit[w] = visit[v] + 1
                    # visit [v]를 고정시켜 v 이후의 w들에 대해 +1 씩 방문 정보 저장
        return visit

    # BFS의 리턴값 visit의 정보를 받은 후
    ans = BFS(S)
    # 최대값을 찾고
    # 값이 중복된 경우 가장 큰 값을 반환하기 위해
    # 조건을 > 이 아닌 >= 으로 설정
    max_idx = 0
    for i in range(101):
        if ans[i] >= ans[max_idx]:
            max_idx = i
    print('#{} {}'.format(t,max_idx))