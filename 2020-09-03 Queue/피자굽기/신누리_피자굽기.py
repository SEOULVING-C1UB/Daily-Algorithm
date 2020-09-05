import sys
sys.stdin = open("(5099)피자 굽기_input.txt")


def cheese():
    global here
    while True:
        idx = (here + 1) % N
        Q[idx] //= 2
        here = idx
        if 0 in Q:
            break


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    # 화덕, 첫 N개를 담고 시작
    Q = temp[0:N]
    # 몇번 피자가 들어있는지 담을 배열, 피자는 0 ~ M-1번.
    # 처음에는 0 ~ N-1 번 피자를 담고 시작
    o = list(range(N))
    # 화덕의 몇번째 자리가 지금 입구에서 보이는지.
    # 초기값은 피자를 전부 넣은 상태이므로 마지막 인덱스.
    here = N - 1

    # M개의 피자를 넣는 과정
    for piz in range(N, M):
        # 빈 곳을 만드는 치즈 녹이기 과정
        cheese()
        # 빈 곳이 생겼으니, Q에 넣어주고, 몇번째 피자인지 o에 저장. 
        Q[here] = temp[piz]
        o[here] = piz

    # 이제 피자가 전부 들어갔으니, 치즈를 녹이며 마지막 피자를 찾는다.
    while True:
        # 인덱스를 늘려가며 피자 한 판의 치즈를 녹이고
        idx = (here + 1) % N
        Q[idx] //= 2
        # 만약 화덕에 피자가 하나 남았다면 break
        if N - Q.count(0) == 1:
            break
        here = idx
    
    # 화덕의 몇번째에 위치한 피자인지 찾아서, 그게 몇번 피자인지 저장
    for i in range(N):
        if Q[i] != 0:
            result = o[i]
    print('#{} {}'.format(t + 1, result + 1))

