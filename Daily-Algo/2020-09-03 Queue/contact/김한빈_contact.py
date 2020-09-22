import sys

sys.stdin = open('Contact.txt', 'r')
for t in range(1, 11):
    print(f'#{t}', end=" ")
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    lines = []
    for i in range(0, len(arr), 2):
        lines.append((arr[i], arr[i + 1]))

    Start = [S]
    End = []
    nodes = set(arr)
    nodes.remove(S)
    while True:
        lasts = []
        End = []
        i = 0
        for line in lines:
            for s in Start:
                # 시작 노드 확인 후, 도착 노드가 아직 살아 있으면
                if line[0] == s and line[1] in nodes:
                    # 도달 노드 제거
                    if line[1] in nodes:
                        nodes.remove(line[1])
                    # 도달 노드, 시작 노드로 바꾸기

                    End.append(line[1])
                    lasts.append(line[1])
                    i = 1
        if lasts != []:
            result = max(lasts)
        Start = End
        if i == 0:
            break
    print(result)
