def check():
    global flag
    for i in range(0,len(info),3):
        dict[info[i]] -= 1              # 무늬에 해당하는 dict에서 1을 빼준다
        if (info[i],int(info[i+1])*10 + int(info[i+2])) not in visited:     # (무늬, 숫자)형식으로 visited에 저장
            visited.append((info[i],int(info[i+1])*10 + int(info[i+2])))    # 만약 카드가 이미 한번 나왔으면
        else:                                                               # 0을 flag에 저장후 return 해준다
            flag = 0
            return

for c in range(int(input())):
    info = list(input())
    dict = {'S': 13, 'D': 13, 'H': 13, 'C': 13}     # 카드덱을 만들어준다
    flag = 1
    visited = []
    check()
    print('#{}'.format(c+1), end= ' ')
    if flag == 1:                                   # flag = 1(참)일때 딕셔너리의 value를 프린트해준다
        for i in dict.values():
            print(i, end=' ')
    else:                                           # flag = 0(거짓)일때 'ERROR'을 프린트해준다
        print('ERROR', end='')
    print()
