# 떠오르는 대로 바로 작성한 것이라서 코드가 정리되지 않을 수 있음
testcase = int(input())
for T in range(testcase):
    N, M = map(int, input().split())
    city_dict = {}              # 서로 알고 있는 관계를 담을 dict
    for i in range(1, N+1):
        city_dict[i] = set()    # 'i' 인간이 알고 있는 사람을 담을 set를 dict에 추가
    city_clan = []              # 창용마을에 있는 패거리 list
    for i in range(M):
        relation = list(map(int, input().split()))
        city_dict[relation[0]].add(relation[1])     # relation[0] 인간은 relation[1] 인간을 알고 있다
        city_dict[relation[1]].add(relation[0])     # relation[1] 인간도 relation[0] 인간을 알고 있다
    for key in city_dict:
        if len(city_clan):          # 창용마을 패거리가 하나라도 있으면
            for clan in city_clan:  # 어떤 패거리 소속 인간인지 확인하고
                if key in clan:
                    break
            if key in clan:
                continue            # 아무 소속도 아니라면
        new_clan = []               # 그 인간을 기준으로 새로운 패거리 형성
        stack = {key}               # 스택에 그 인간 넣기(중복 삽입을 줄이기 위해 set로)
        while len(stack):           # 이후 dfs
            key = stack.pop()
            if key in new_clan:     # 새로운 패거리에 합류한 사람이면 또 세지는 않도록
                continue
            new_clan.append(key)
            if not len(city_dict[key]):     # 그 인간이 고독하다면 break 하고 혼자 두기
                break
            for new_key in city_dict[key]:  # 그 인간이 알고 있는 모든 사람을
                if new_key not in new_clan: # 새로운 패거리에 없다면 stack에 넣기
                    stack.add(new_key)      # stack이 비었다면 합류할 수 있는 사람 모두가 합류했다는 뜻이므로
        city_clan.append(new_clan)          # 이를 창용마을 패거리로 등록
    print('#{} {}' .format(T+1, len(city_clan)))