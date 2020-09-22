'''
<기본컨셉>
1) bfs를 기본컨셉으로 한다
2) 시작점으로 부터 연결된 모든 친구들을 now리스트에 넣으면서 방문표시를 한다.
3) now리스트는 contacted로 바꾸고 현재시점의 연락받은 친구들이다
4) 다시 그친구들로 부터 연락받지 않은 친구들을 now에 넣기를 now에 원소가 없을때 까지 반복
5) 마지막으로 contacted에 남아있는 친구들중 가장 큰 번호를 출력한다.

<주의사항>
1) bfs배우기 전에 짠거라 좀엉성한데.. 다시짜면 더 잘 짤수 있을까..
'''


for i in range(1, 11):
    n, s = map(int,input().split())
    lst = list(map(int, input().split()))
    fts = []                                                # from to 리스트를 입력할 리스트
    for j in range(0,n,2):
        if [lst[j], lst[j+1]] not in fts:                   # 중복되는 ft도 존재하므로 중복 확인후 apprend
            fts.append([lst[j], lst[j+1]])
    fts.sort()                                              # 크기순 정렬
    visited = [s]                                           # 방문 표시용 리스트
    contacted =[s]                                          # 현재 연락하는 친구들 리스트
    while True:
        now = []                                            # 현재 연락받은 친구들 저장할 리스트
        for fr in contacted:                                # 현재 연락하는 친구들 fr
            for ft in fts:
                if ft[0] == fr and (ft[1] not in visited):  # 현재 연락하는 친구가 연락받지 않은 친구에게 연락
                    now.append(ft[1])                       # 현재 연락받은 친구에 추가
                    visited.append(ft[1])                   # 방문 표시
        if len(now) == 0:                                   # 연락받을은 친구가 없으면 브레이크
            break
        contacted = now                                     # 연락 받은친구들을 현재 연락하는 친구들로 변경
    print(f'#{i} {max(contacted)}')                         # 마지막으로 연락받은 친구들중 가장 높은 숫자 출력