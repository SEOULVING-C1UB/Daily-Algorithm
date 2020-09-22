T = int(input())
# 상,하,좌,우 탐색
dr = [-1,1,0,0]
dc = [0,0,-1,1]

for t in range(1,T+1):
    # 입력값
    N = int(input())
    room = [list(map(int,input().split()))for _ in range(N)]
    # 매개변수
    max_val = 1     # 갈 수 있는 방을 count한 후 최대값을 비교하기 위한 매개변수
    min_idx = N * N # 최소 index 를 찾기 위한 매개변수
    # 순회하며 완전탐색
    for r in range(N):
        for c in range(N):
            cnt = 1         # 첫 방문 한 방의 개수를 counting하며 시작
            S = []
            S.append([r,c]) # 스택 구조를 사용하여, 초기 좌표를 입력
            visit = [[0]*N for _ in range(N)]   # 초기 좌표 입력에 따라 visit을 매번 초기화
            # DFS 시작
            while len(S):
                V = S.pop()
                vr = V[0]
                vc = V[1]
                visit[vr][vc] = 1
                for i in range(4):
                    nr = vr + dr[i]
                    nc = vc + dc[i]
                    if nr <0 or nr == N or nc < 0 or nc == N: continue
                    if visit[nr][nc] == 1:continue
                    if room[nr][nc] - room[vr][vc] == 1:        # 이동한 방 - 기준 방의 차이가 1인 경우만 append
                        S.append([nr,nc])
                        cnt += 1                                # 방 이동 후 cnt 1 증가
                        break                                   # 모두 숫자가 다르므로 1이 차이나는 경우는 1개 존재하여 break로 탈출
            # 최대 값을 찾기 위한 탐색
            if cnt > max_val:
                max_val = cnt
                min_idx = room[r][c]
            # 같은 경우 최소 인덱스를 비교
            elif cnt == max_val:
                if room[r][c] < min_idx:
                    min_idx = room[r][c]
    print('#{} {} {}'.format(t,min_idx,max_val))
