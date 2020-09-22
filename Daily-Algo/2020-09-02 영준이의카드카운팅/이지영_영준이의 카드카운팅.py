T = int(input())

for tc in range(1, T+1):
    
    # 먼저 영준이의 카드들을 입력받는다
    yj = input()
    
    # 카드는 총 13개가 있어야하니까 14까지 있는 배열을 만들어서 value에 넣어줌
    cards = {
        'S':[0 for _ in range(14)],
        'D':[0 for _ in range(14)],
        'H':[0 for _ in range(14)],
        'C':[0 for _ in range(14)]
    }
    
    # 이제 영준이가 가진 패를 돌릴거다
    for i in range(len(yj) - 2):

        # 3의 배수들은 다 카드종류니까 그때마다 멈춤
        if i%3 == 0:
            tmp = cards.get(yj[i])      # 현재 카드 종류의 value를 들고와서
            idx = int(yj[i+1]+yj[i+2])  # 카드 종류 뒤에 숫자 두자리를 알아내고
            tmp[idx] += 1               # value가 배열이니까 알아낸 숫자(=인덱스)에 1을 증가시켜줌
            cards[yj[i]] = tmp          # 그걸 다시 딕셔너리에 넣어준다
    
    # 결과 담을 리스트
    result = []
    
    for v in cards.values():    #value들만 돌려서
        cnt = 0 #몇개 비었는지 셀거

        for i in range(len(v)): #각 value는 리스트니까 걔를 돌린다    
            if v[i] >1:
                result.append('error')  #1보다 많으면 중복이니까 에러
                break
    
            elif v[i] == 0: #그게 아니라 그냥 0이면 비었다고 1증가시켜줌
                cnt += 1
        result.append(cnt-1)   #인덱스 0은 포함안되니까 1빼주기
    
    if 'error' in result:
        print('#{} ERROR'.format(tc))
    else:
        print('#{}'.format(tc), *result, sep=' ')
