'''
[컨셉]
1) 수업시간에 배운 진입차수 + dfs
'''

for t in range(1, 11) :
    V, E =map(int, input().split())
    temp = list(map(int, input().split()))
    arr = [[0]*(V+1) for _ in range(V+1)]   # 인접 행렬에 입력을 넣음
    for i in range(E) :
        s, e = temp[2*i], temp[2*i+1]
        arr[s][e]  = 1
    
    inord = [0]                             # 진입차수를 넣기 위한 list
    for i in range(1, V+1) :                # 1~N 번에 대해 진입차수 구하기
        temp = 0
        for j in range(1, V+1) :
            temp += arr[j][i]
        inord.append(temp)

    print('#{} ' .format(t), end='')        # 출력의 첫부분(#{tc}) 먼저 해주고
    s = []                                  # stack에 진입차수가 0인 것들 담기
    for i in range(1, V+1) :
        if inord[i] == 0 :
            s.append(i)

    while s :                               # dfs
        v = s.pop()
        print(v, end=' ')                   # 정점 방문하면 print
        for w in range(V+1) :               
            if arr[v][w] == 1 :             # v와 인접한 w에 대하여
                inord[w] -=1                # 진입차수를 하나 줄여주고
                if inord[w] == 0 :          # 진입차수가 0이 되면
                    s.append(w)             # stack에 추가
    print()