'''
기본 컨셉
1) 화덕 리스트를 만들어 인덱스를 돌려가며 //2 연산
2) //2 연산후 치즈가 없으면 대기 리스트의 피자로 교체
3) 대기 리스트에 피자가 없으면 화덕 리스트에서 제거
4) 화덕에 피자가 한개 남으면 그 피자의 인덱스 출력

주의사항
1) 화덕 피자수가 달라지기 때문에 for문으로 돌리면 인덱스에러가 잘남
2) 원형 큐를 구현해야하므로 인덱스에 나머지 연산 사용
'''

import sys
sys.stdin = open("5099_피자굽기.txt")

t = int(input())

for i in range(1, t+1):
    n, m = map(int,input().split())
    pizzas = list(map(int,input().split()))         # 피자들 저장
    pizzas_num = []                                 # 각 피자에 번호 부여할 리스트
    for idx, p in enumerate(pizzas):
        pizzas_num.append([idx+1, p])               # 피자에 번호 붙여서 리스트로 만든후 pizza_num에 저장
    hwaduck = pizzas_num[:n]                        # 처음에 화덕에 들어갈 피자들 n개
    now = n                                         # 새로운 피자를 넣기 위한 대기열 인덱스
    j = 0                                           # while문 인덱스
    while True:
        hwaduck[j][1] //= 2                         # 화덕을 돌면서 //2 연산
        if hwaduck[j][1] == 0:                      # 치즈가 없으면
            try:                                    # 대기 피자가 없을수 있으므로 try문 사용
                hwaduck[j] = pizzas_num[now]        # 현재 화덕위치에 대기피자 저장
                now += 1                            # 대기열 인덱스 1 증가
                j = (j+1)%len(hwaduck)              # while문 인덱스 1 증가후 화덕 크기로 나눈 나머지를 인덱스로 사용. 원형 큐 구현
            except:                                 # 대기 피자가 없으면
                del hwaduck[j]                      # 화덕에서 피자 빼
                if len(hwaduck) == 1:               # 화덕에 피자가 한개 남으면 그게 답
                    print('#{} {}'.format(i, hwaduck[0][0]))
                    break
                else:
                    j = j%len(hwaduck)              # 화덕에 피자가 한개 빠졌으므로 인덱스 증가없이 나머지 연산만
        else:
            j = (j+1)%len(hwaduck)                  # 치즈가 있으면 인덱스만 수정