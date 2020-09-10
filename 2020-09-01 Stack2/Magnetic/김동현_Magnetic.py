for tc in range(1,11):
    T=int(input())
    al=[]
    for q in range(100):
        a=list(map(int,input().split()))
        al += [a]
    cnt = 0
    for i in range(100):
        for j in range(99): # j 값에는 +1을 할 것이기 때문에 99까지만
            if al[j][i] == 1: # 붉은 자성체인지 확인
                if al[j+1][i] == 0: # 빈칸이면 붉은 자성체가 이동한 것으로 확인
                    al[j+1][i] = 1
                elif al[j+1][i] == 2: # 푸른 자성체 만나면 cnt +1 해주고 그 다음부터 다시 붉은 자성체 찾아서 반복하면 됨
                    cnt += 1 # 어짜피 붉은 자성체가 몇 개있든 푸른 자성체를 만나면 멈춰야하기 때문에

    print('#{} {}'.format(tc, cnt))