'''
<기본컨셉>
 : 재귀호출로 부분집합의 합 구현
1) i번째 사람을 넣은 경우와 넣지않은 경우로 재귀호출
2) 이 과정을 마지막 사람까지 반복한 후 B보다는 크거나 같고 현재 최솟값 보다 작으면 갱신
3) 과정중 최솟값을 넘어가면 가지치기

<추가사항>
1) 자기 손만 닿는곳에 물건을 두다니.. 장훈이는 개인주의야...
'''

def tower(i, N, s):
    global min_s                        # 전역변수 설정
    if s > min_s:                       # 가지치기
        return
    if i == N:                          # 마지막 도달 후 갱신 여부 확인
        if B <= s < min_s:
            min_s = s
    else:
        tower(i+1, N, s+heights[i])     # i번째를 넣은 경우
        tower(i+1, N, s)                # i번째를 안 넣은 경우
    
t = int(input())

for i in range(1,t+1):
    N, B = map(int,input().split())
    heights = list(map(int,input().split()))
    min_s = 100000000                   # 항상 최솟값은 충분히 크게
    tower(0, N, 0)
    print('#{} {}'.format(i,min_s-B))
