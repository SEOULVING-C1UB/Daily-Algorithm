from itertools import product

import sys

sys.stdin = open("D4_4613_input.txt", "r")
    

def flag_change():
    # 가능한 최대 색칠 횟수
    result = 2500

    # 흰색, 파란색, 붉은색 줄의 갯수를 나타내는 w, b, r의 조합을 다 따짐
    for com in product(range(1,n-1), range(1,n-1), range(1,n-1)):
        # 세 변수의 합이 n이 되는 경우에만 계산
        if sum(com) == n:
            w, b, r = com[0], com[1], com[2]
        else:
            continue
        
        # 각 조합에 대해서 새로 색칠을 해야하는 횟수 temp
        temp = 0
        for i in range(n):
            # 하얀색 범위에서, 깃발에 푸른색이나 붉은색이 있으면 temp+=1
            if i < w:
                for j in range(m):
                    if flag[i][j] in ['B', 'R']:
                        temp += 1
            elif i < w+b:
                for j in range(m):                
                    if flag[i][j] in ['W', 'R']:
                        temp += 1
            else:
                for j in range(m):                
                    if flag[i][j] in ['B', 'W']:
                        temp += 1
            # 가지치기: 한 줄을 다 칠할 때마다 현재 최솟값인 result와 temp 비교
            if temp > result:
                break
        
        # 깃발을 전부 새로 칠했을 때 그 횟수가 result보다 적다면 갱신
        if temp < result:
            result = temp
    
    return result

T = int(input())
for test_case in range(T):
    
    n, m = map(int, input().split())
    flag = [input() for _ in range(n)]
    print('#' + str(test_case + 1), flag_change())    
