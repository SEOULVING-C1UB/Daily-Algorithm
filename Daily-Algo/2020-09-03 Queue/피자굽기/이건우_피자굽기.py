import sys
sys.stdin = open('피자_input.txt', 'r')

def pizza():
    # 화로에 피자를 채운다
    for i in range(N):
        T[i] = i+1
        Q[i] = C[i]
    # 몇번째 피자부텀 못채웠는지 표시
    index = N
    while True:
        # 가장 먼저 넣은 피자부터 구운다 (치즈//2)
        tempQ = Q[0]//2
        # 치즈가 남아있으면 가장 앞에있는 피자를 꺼내서 뒤로 보낸다 (회전시키는거와 같은 원리)
        if tempQ != 0:
            Q.pop(0)
            Q.append(tempQ)
            # i 번째로 넣은 피자의 위치를 같이 회전시켜준다
            tempT = T[0]
            T.pop(0)
            T.append(tempT)
        # 치즈가 모두 구워지면 (치즈 ==0) 꺼내고 뒤에 새 피자를 넣는다
        else:
            Q.pop(0)
            T.pop(0)
            # 넣을 피자가 있을시에만 넣어준다
            if index < len(C):
                Q.append(C[index])
                T.append(index+1)
                index += 1
            # 마지막 남은 피자가 몇번째로 넣은 피자인지 return한다
            if len(T) == 1:
                return T[0]

for c in range(1, int(input())+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    Q = [0] * N
    T = [0]*N
    print('#{} {}'.format(c, pizza()))
