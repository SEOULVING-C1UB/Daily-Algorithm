'''
<접근방법>
 : 가로, 세로별 가장 넓은 길이를 찾아 둘을 곱하면 최댓값이다.
 1) 가로, 세로 각각 자른 좌표를 저장한다.
 2) 잘라진 좌표의 차이들 중 최대를 각각 찾아 곱한다.
<주의사항>
 1) 가로로 자르면 세로 좌표가 그어지는거고 세로로 자르면 가로 좌표가 그어지는거다 헷갈리지 말자
'''

g, s = map(int,input().split())

paper = [[0, s], [0, g]]                # 잘라진 위치를 저장할 리스트. 맨 처음과 맨 끝도 저장
ans = 1                                 # 정답을 담을 초깃값. 가로, 세로 최대값을 곱할거라 1로 설정
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    paper[a].append(b)                  # 가로, 세로에 각각 좌표를 담고
paper[0].sort()                         # 정렬
paper[1].sort()

for i in range(2):
    max_l = 0                           # 최댓값 초기화
    for j in range(len(paper[i])-1):
        l = paper[i][j+1]-paper[i][j]   # 현재 길이
        if l > max_l:                   # 최댓값 갱신
            max_l = l
    ans *= max_l
print(ans)