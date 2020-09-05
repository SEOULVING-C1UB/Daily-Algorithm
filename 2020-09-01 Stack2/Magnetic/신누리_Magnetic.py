for a in range(10) :
    N = int(input())
    mat =[]
    for n in range(N) :
        row = list(map(int, input().split()))
        mat.append(row)
    # 교착 상태 개수 저장
    cnt = 0
    # 배열을 순회하며
    for i in range(N) :
        # 열을 list에 담고
        col =[]
        for j in range(N) :
            if mat[j][i] :
                col.append(mat[j][i])
        # 열을 기준으로, 1,2가 붙게 되면 cnt+1
        for k in range(len(col)-1) :
            if col[k] == 1 and col[k+1] ==2 :
                cnt+=1
    print('#{} {}' .format(a+1, cnt))
    