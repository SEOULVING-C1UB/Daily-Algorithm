'''
<문제해결>
 : 카드를 받을때 마다 방문체크하여 런 or 트리플렛을 확인.
1) 각 번호별 체크리스트 생성
2) 현재 받은 카드를 체크리스트에 추가
3) 런과 트리플렛을 확인하여 결과 반환

<추가사항>
1) 1번이 성공하면 바로 승리하니 상당히 1번에게 유리한게임..
'''

import sys
sys.stdin = open("5203_베이비진게임.txt")


def babygin(lst):                       # 런과 트리플렛 확인하는 함수
    check = [0 for _ in range(10)]      # 번호별 카드 갯수 저장하는 리스트
    for num in lst:
        check[num] += 1                 # 카드 번호에 맞춰 값 증가
    if 3 in check:                      # 트리플렛 존재 확인
        return 1
    else:                               # 런 존재 확인
        cnt = 0
        for c in check:
            if c:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                return 1
    return 0                            # 순회 후 런, 트리플렛 없으면 0반환


t = int(input())

for tc in range(1, t+1):
    cards = list(map(int, input().split()))
    for i in range(4):
        p_1 = cards[:5+2*i:2]           # 1번 플레이어의 현재 카드
        p_2 = cards[1:6+2*i:2]          # 2번 플레이어의 현재 카드
        if babygin(p_1):                # 1번 플레이어 확인하여 성공하면 1번 승리
            ans = 1
            break
        elif babygin(p_2):              # 1번이 실패한 경우 2번이 성공하면 2번 승리
            ans = 2
            break
    else:                               # 모든 경우 순회 후 무승부
        ans = 0
    print(f'#{tc} {ans}')