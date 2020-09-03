import sys
sys.stdin = open('회전_input.txt')

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    numList = list(map(int, input().split()))

    # 진짜 말그대로 앞에걸 빼서 뒤에 넣었다...
    while M>0:
        numList.append(numList.pop(0))
        M -= 1

    print('#{} {}'.format(tc, numList[0]))
