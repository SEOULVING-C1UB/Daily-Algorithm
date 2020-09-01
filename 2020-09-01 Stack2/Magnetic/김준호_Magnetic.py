T = 10

def findStop(mat):
    count = 0
    for i in range(100):
        case = 0
        for j in range(99):
            if mat[j][i] == 1 and mat[j+1][i] == 2:
                count += 1
                case = 0
                continue
            if mat[j][i] == 1 and (mat[j+1][i] == 1 or mat[j+1][i] == 0):
                case = 1
                continue
            if case == 1 and mat[j+1][i] == 2:
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