T = 10

def findStop(mat):
    count = 0
    for i in range(100):    # 가로
        case = 0            # 2가 나오기 전에 1이 나왔다면 1 아니라면 0
        for j in range(99): # 세로
            if mat[j][i] == 1 and mat[j+1][i] == 2: # 교착 상태
                count += 1
                case = 0
                continue
            if mat[j][i] == 1 and (mat[j+1][i] == 1 or mat[j+1][i] == 0):   # 1이 나온상황이므로 case 전환
                case = 1
                continue
            if case == 1 and mat[j+1][i] == 2:  # 1이 나온적이 있고 2가 나왔으므로 교착+1, case 초기화
                case = 0 
                count += 1
                continue
    return count

for test_case in range(1, T + 1):
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))
    print(f'#{test_case} {findStop(mat)}')