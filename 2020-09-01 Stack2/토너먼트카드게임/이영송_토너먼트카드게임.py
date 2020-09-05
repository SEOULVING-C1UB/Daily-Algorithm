'''
컨셉
1. 카드 뭉치의 처음과 끝 값이 같아질 때까지 쪼갭니다.
    [= 카드 뭉치의 총 개수가 1개가 될 때까지]
2. 나누기 위해 재귀 함수를 만들었습니다.
    2.1 나누는 함수는 처음과 끝을 인덱스 정보로 받습니다.
    2.2 함수에 삽입되면 둘을 반으로 나누고
    2.2 (처음 - 반) / (반- 끝)으로 두 번 호출합니다.
3. check함수로 가위바위보 시킵니다.
    3.1. 한 쪽을 기준으로 작성해서 이기는 경우의 수를 나누고
    3.2. 나머지는 다 다른 쪽이 이긴다고 했습니다.
4. 결과 인덱스는 1부터 시작하므로 +1로 보정합니다.
'''

import sys; sys.stdin = open('tournament_input.txt')

T = int(input())

# A를 기준으로 작성된 가위바위보, 나머지는 모두 B의 승리
def check(i,j):
    if cards[i] == cards[j] : return i
    elif cards[i]==1 and cards[j]==3 : return i
    elif cards[i]==2 and cards[j]==1 : return i
    elif cards[i]==3 and cards[j]==2 : return i
    else : return j

# 처음과 나중의 길이가 같아질 때 까지 == 원소가 1개 남을 떄까지
def tournament(i,j):
    if i==j :
        return i
    else:
        m = (i+j)//2+1
        # m을 매게하여 계속 재귀 함수를 호출합니다.
        return check(tournament(i,m-1),tournament(m,j))

for t in range(1,T+1):
    N = int(input())
    cards = list(map(int,input().split()))

    i = 0               # 초기 시작은 0
    j = len(cards) - 1  # 초기 끝지점은 n-1

    print('#{} {}'.format(t,tournament(i,j)+1))  #인덱스 보정 +1