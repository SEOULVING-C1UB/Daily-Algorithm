def oven():
    oven_in = []
    oven_out = []
    # 오븐에 들어갈 수 있는 수(n)만큼의 길이를 갖는 리스트 생성
    for i in range(n):
        oven_in.append(p_list[i])
    
    # cnt는 p_list의 인덱스를 나타냄
    # 오븐에서 피자가 나오면 p_list에서 피자를 꺼내 오븐에 채움
    cnt = n
    f = 0    
    while True:        
        # 치즈가 0이 되었으면 피자를 빼야 함
        # 뺀 피자는 oven_out에 저장하고, 하기전에 유효성 검사  
        # cnt==m이 되면(모든 피자가 오븐에 들어가면) p_list에서 빼지않음
        if oven_in[f][0] == 0:            
            if oven_in[f] not in oven_out:
                oven_out.append(oven_in[f])
            if cnt < m:
                oven_in[f] = p_list[cnt]
                cnt += 1

        # 모든 피자가 오븐에서 나오면 top값을 읽어 인덱스를 리턴
        if len(oven_out) == m:
            return oven_out[-1][1]

        f += 1
        
        # 오븐 내의 피자를 한번씩 다 보면 치즈를 녹임
        if f == n:
            for pizza in oven_in:
                pizza[0] //= 2
            f = 0


T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    c_list = list(map(int, input().split()))    

    # 1번부터 m번까지의 피자 번호와 각각에 뿌려진 치즈의 양
    p_list = [[c_list[i], i+1] for i in range(m)]
    print('#' + str(test_case + 1), oven())