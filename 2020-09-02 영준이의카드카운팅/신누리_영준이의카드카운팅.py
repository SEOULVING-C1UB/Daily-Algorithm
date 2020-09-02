T = int(input())
for t in range(T) :
    # 입력을 list로 받아온다
    temp = list(input())
    # 모양을 나타내는 알파벳 저장
    shape = ['S', 'D', 'H', 'C']
    # 각 모양 별로 [0]은 비워두고, 13개의 카드를 확인하기 위해 14*4 배열을 만들어 0으로 초기화한다.
    confirm = [[0]*14 for _ in range(4)]
    # 에러가 났는 지를 확인하기 위해 flag 사용
    flag = True
    # 입력을 3개 단위로 끊어서 읽는다
    for i in range(0, len(temp), 3) :
        # 첫 값인 알파벳이 무슨 모양에 속하는지 확인하고, 그 index 값을 저장해둔다.
        for k in range(4) :
            if temp[i] == shape[k] :
                idx = k
                break
        # num에는 몇번 카드인지를 저장한다.
        num = ""
        # 만약 10의 자리가 1이라면 문자열에 넣어주고
        if temp[i+1] == "1" :
            num += temp[i+1]
        # 1의 자리는 무조건 넣어준다.
        num += temp[i+2]
        # 문자열을 int로 변환한다.
        num = int(num)
        # 그 카드가 없다면, 카드를 보유하고 있다는 의미에서 1을 넣어준다.
        if confirm[idx][num] == 0 :
            confirm[idx][num] = 1
        # 이미 그 카드를 가지고 있다면, flag를 False로 바꾸고 에러임을 출력한다.
        else :
            flag = False
            print('#{} ERROR' .format(t+1))
    # 만약 에러 없이 주어진 입력을 모두 처리했다면
    if flag :
        print('#{} ' .format(t+1), end="")
        # 4개의 모양에 대해서
        for i in range(4) :
            # 13개 중에 가지고 있는 카드의 개수를 빼서 출력한다.
            print(13-(sum(confirm[i])), end=" ")
        print()