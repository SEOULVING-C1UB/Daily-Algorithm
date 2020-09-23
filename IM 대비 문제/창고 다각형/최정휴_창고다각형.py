'''
<접근방법>
 : 위로 볼록이려면 가장 높은곳을 향해 왼쪽과 오른쪽에서 증가 그래프를 그려 나가면 된다.
 1) 1001짜리 리스트를 만들어 기둥을 저장한다.
 2) 최대 높이기둥이 있는 지점까지는 현재 최대 높이보다 높은 기둥이 나오면 갱신
 3) 최대 높이기둥 이후에서는 맨 끝에서 반대로 최대높이까지 다가오며 위와 같은 방법 사용
'''

n = int(input())
warehouse = [0]*1001                # 1001짜리 창고
max_h = 0                           # 최대 높이는 0으로 초기 설정
ans = 0                             # 총 너비 담을 변수
for _ in range(n):
    l, h = map(int,input().split())
    warehouse[l] = h                # 창고에 기둥 저장
    if h > max_h:                   # 최대 높이 기둥찾아서 위치 저장
        max_h = h
        max_l = l
now = 0                             # 현재기둥 높이 0으로 초기화
for i in range(max_l):              # 최대 높이 기둥까지 왼쪽에서 접근
    if warehouse[i] > now:          # 현재 최대 높이보다 큰 기둥을 만나면 갱신
        now = warehouse[i]
    ans += now                      # 어차피 너비가 1이므로 기둥 높이가 면적. ans에 저장
now = 0                             # 반대로 돌아오는 반복문 돌리기 전에 최대기둥높이 초기화
for i in range(1000, max_l-1, -1):  # 최대 높이 기둥까지 오른쪽에서 접근
    if warehouse[i] > now:
        now = warehouse[i]
    ans += now
print(ans)