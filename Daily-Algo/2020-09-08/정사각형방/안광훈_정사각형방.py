T = int(input())

for t in range(1, T + 1):
    N = int(input())
    rooms = dict()

    # 숫자별 좌표를 rooms 딕셔너리에 추가
    for r in range(N):
        row = list(map(int, input().split()))
        for c in range(N):
            rooms[row[c]] = [r, c]

    # 방 번호, 방 갯수
    result = [0, 0]

    # 두 방이 인접한지 검사하는 함수
    def is_close(a, b):
        if abs(rooms[a][0] - rooms[b][0]) == 1 and rooms[a][1] == rooms[b][1]:
            return True

        if abs(rooms[a][1] - rooms[b][1]) == 1 and rooms[a][0] == rooms[b][0]:
            return True

        return False

    # k0: 출발점, n: 지나간 방의 개수
    k0 = 1
    n = 1

    for i in range(1, N ** 2):
        # 다음 번호가 인접한 방이라면
        if is_close(i, i + 1):
            n += 1
            continue

        # 지나간 방의 개수가 result 값보다 클 경우
        # 같을 때는 더 작은 번호가 와야 하므로 고려하지 않아도 된다
        if n > result[1]:
            result = [k0, n]

        # 출발점, 방 개수 초기화
        k0 = i + 1
        n = 1

    # 모든 방을 지나고 마지막으로 체크
    if n > result[1]:
        result = [k0, n]

    print('#{} {}'.format(t, ' '.join(map(str, result))))
