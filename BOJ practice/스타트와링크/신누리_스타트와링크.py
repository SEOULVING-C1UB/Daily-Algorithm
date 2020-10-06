'''
[컨셉]
1) 입력을 받아온다.
2) team은 선수 수만큼의 길이를 가진 배열이다. 선택되면 1, 선택되지 않으면 0이다.
  - 계산을 줄이기 위해 팀A에 1번 선수가 포함된 경우만 생각한다.
3) make_team으로 N//2명의 선수를 선택한다.
4) chemistry에서 각 팀의 능력치를 계산해서 그 차를 반환한다.
5) 그 정보를 바탕으로 result를 갱신하여 출력한다.
'''

def chemistry():                                # 두 팀의 능력치의 차 반환
    team_a, team_b = [], []                     # team_a, team_b에 각각 속하는 선수의 idx 저장
    a = b = 0                                   # 각 팀의 능력치를 저장할 변수
    for i in range(N):                          # team_a, team_b 구성
        if team[i] : team_a.append(i)
        else: team_b.append(i)
    for i in range(N//2):                       # 각 팀별로 능력치 계산
        for j in range(N//2):
            a += chemi[team_a[i]][team_a[j]]
            b += chemi[team_b[i]][team_b[j]]
    if a > b: return a - b                      # 능력치의 차 반환
    else: return b - a


def make_team(k, N, s):             # k번 선수 선택 여부 고려, N까지, s명 선택 완료 (편의를 위해 0~N-1번 선수로 가정한다.)
    global result                   # 갱신해야하니 global로
    if k == N:                      # 선택이 끝났고
        if s == N//2:               # 반으로 잘 나뉘면
            chemi = chemistry()     # chemistry로 두 팀의 능력치의 차를 구해서
            if chemi < result:      # 현재 결과 값과 비교해서 갱신한다.
                result = chemi
            
    else:                           # 아직 선택 중이고
        if s <= N//2:               # 선택한 인원이 절반을 넘지 않았다면
            team[k] = 0             # 팀원으로  미선택
            make_team(k+1, N, s)
            team[k] = 1             # 팀원으로 선택
            make_team(k+1, N, s+1)


# 입력 받기
N = int(input())
chemi = [list(map(int, input().split())) for _ in range(N)]

result = 0x7FFFFFFF     # 결과 값 저장할 변수 result에는 큰 정수를 넣는다.

team = [1] + [0]*(N-1)  # a팀의 팀원 선택 여부를 저장할 배열 team
make_team(1, N, 1)      # make_team으로 N//2명의 선수를 선택
print(result)           # 결과 값 저장
