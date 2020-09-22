'''
컨셉
1) 일부러 front rear를 쓰는 C 방식으로 풀어보고자 했습니다
    1-1) 처음에 원형 방식으로 풀다가 덮어쓰기 문제를 해결하지 못했습니다
    1-2) 이에 아주아주 긴 선형구조를 만들었습니다.
    1-3) 최대 선형 길이는 원소의 개수 + 반복 회수 이므로
    1-4) 초기값을 0, 인덱스를 1부터 읽기 위해 N + M + 1의 선형 큐를 만듭니다
2) 만들어진 선형 큐에 초기 값을 할당합니다.
3) M번 반복하며 deQ와 enQ를 반복합니다.
    3-1) 이 때 is Full 이나 is Empty는 필요 없습니다.
    3-2) deQ는 읽어오기의 기능정도 밖에 되지 않기 떄문에
    3-3) deQ를 하고 나면 항상 front자리를 0으로 초기화 시켜 줍니다.
4) front자리에는 원소가 없기 때문에
    4-1) 정답으로 선형 큐의 front + 1 번째 원소를 출력합니다.
'''

import sys
sys.stdin = open('(5097)_input.txt')

T = int(input())

def enQ(item):
    global front, rear
    rear += 1
    Q[rear] = item

def deQ():
    global front, rear
    front += 1
    return Q[front] # deQ는 값을 읽어오기 밖에 안합니다

for t in range(1,T+1):
    N,M = map(int,input().split())
    tmp = list(map(int,input().split()))
    Q = [0] * (N+M+1)
    front = 0
    rear = N                #rear의 경우에는 초기에 이미 N개의 원소가 삽입되어 있습니다.
    for i in range(N):
        Q[i+1] = tmp[i]

    for m in range(M):      # m번 반복하며 deQ를 하고, enQ를 합니다.
        value = deQ()
        Q[front] = 0        # deQ는 값을 불러오므로 초기화 장치를 새로 설정합니다.
        enQ(value)

    print('#{} {}'.format(t,Q[front+1])) #front+1 의 값 = 가장 첫 원소를 출력합니다.