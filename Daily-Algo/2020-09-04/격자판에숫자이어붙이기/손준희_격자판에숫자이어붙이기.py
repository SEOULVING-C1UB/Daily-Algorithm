import sys
sys.stdin = open('grid_input.txt', 'r')

movement = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 좌 우 상 하

def num_worm(ans_set, word, x, y):
    for move in movement:                           # 좌, 우, 상, 하 순서대로
        nextX, nextY = x + move[0], y + move[1]     # 다음 목표 위치를 받는다
        if -1 < nextX < 4 and -1 < nextY < 4:
            word += table[nextY][nextX]             # 해당 목표 위치의 숫자를 뒤에 늘린다
            if len(word) < 7:                           # 7개의 숫자가 안 모이면
                num_worm(ans_set, word, nextX, nextY)   # 재귀호출
                word = word[:len(word)-1]               # 재귀호출이 끝나면 재귀 호출에서 붙인 숫자를 1개 반납
            else:                   # 숫자 7개가 모였다면
                ans_set.add(word)   # 이를 set에 추가
                word = word[:6]     # 그리고 방금 붙인 숫자 1개를 떼내고 함수 종료

testcase = int(input())
for i in range(testcase):
    table = [input().split()[:4] for j in range(4)]
    ans_set = set()
    for y in range(4):          # 매 행마다
        for x in range(4):      # 매 열마다
            word = table[y][x]  # 시작 숫자를 하나 가져온다
            num_worm(ans_set, word, x, y)   # 그리고 dfs 시작
    print('#{} {}' .format(i+1, len(ans_set)))
