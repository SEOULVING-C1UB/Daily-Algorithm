'''
[컨셉]
* subsetsum 문제
1) 입력을 받아오고, 결과값을 저정할 maxi는 0으로 초기화한다.
2) subsetsum 함수를 통해, 선택/미선택 여부에 따라 계속 함수를 돌려, 최댓값을 갱신한다.
'''

def subsetsum(k, n, add):                   # subset sum 함수
    global maxi                             # 최댓값 갱신해야 하니 maxi를 global로 사용
    if k == n:                              # 퇴사 날이 다가왔다면 
        if add > maxi :                     # 최댓값 갱신
            maxi = add
    elif k < n :                                            # 퇴사하기 전까지는
        subsetsum(k+1, n, add)                              # 해당 일에 상담 안할 때 : 다음 날 상담 확인하기
        subsetsum(k+counsels[k][0], n, add+counsels[k][1])  # 해당 일에 상담 할 때 : 다음 상담 가능 일 확인, 번 돈 더하기

# 입력 받아오기
N = int(input())                            # N days                            
counsels = [0]                              # 상담 일수, 액수 저장. 0일로 생각하지 않도록 데이터 하나 넣고 시작.
for n in range(N):
    days, pay = map(int, input().split())
    counsels.append([days, pay])

maxi = 0                                    # 결과값을 저장할 변수
subsetsum(1, N+1, 0)                        # 1일부터, N+1일(N일째까지 일하는 것)까지, 얼마 벌었는지.
print(maxi)                                 # 결과 출력
