import sys

sys.stdin = open("D3_1220_input.txt", "r")

# 1: N, 2: S
def magnet():
    cnt = 0
    # 위에 N극 아래에 S극이므로 행을 먼저 scan
    for j in range(100):        
        temp = 0
        for i in range(100):
            if table[i][j] == 0:
                pass
            elif table[i][j] == 1:
                if temp == 0:
                    temp = 1
            else:
                # N다음에 S가 오는 것이 교착상태가 되므로 이 경우에만 카운트
                if temp == 1:
                    temp = 0
                    cnt += 1
    return cnt


for test_case in range(10):
    t = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    print('#' + str(test_case + 1), magnet())
