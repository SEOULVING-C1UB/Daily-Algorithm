'''
<접근방법>
 : 별이 가장쎄니 가장 높은 점수로두면 되지않을까? 별의 갯수 *1000, 동그라미 *100 이런식으로 하면 서로에게 영향을 주지 않을테니 구현해보자
 1) 우선 무늬의 갯수가 100이하 이므로 각무늬별 자릿수의 차이는 세개는 나야한다.
 2) 따라서 1000을 기준으로 세모갯수는 그대로, 네모갯수*1000, 동그라미*(1000**2), 별*(1000**3)이렇게 하면 서로 간섭하지 않는 단일숫자가 만들어진다.
 3) 그후 대소비교하면 끝
'''

n = int(input())

for _ in range(n):
    a = list(map(int,input().split()))[1:]  # a, b의 무늬를 받아오고 필요없는 첫 숫자는 날린다.
    b = list(map(int,input().split()))[1:]
    a_score = b_score = 0                   # 점수 0으로 초기화
    for ddakzi in a:
        a_score += 1000**(ddakzi-1)         # 각 무늬가 4,3,2,1 순서를 가지고 있으므로 1을 빼서 지수로 활용
    for ddakzi in b:
        b_score += 1000**(ddakzi-1)
    if a_score > b_score:                   # 결과 확인
        print('A')
    elif a_score < b_score:
        print('B')
    else:
        print('D')