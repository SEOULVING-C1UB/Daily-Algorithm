import sys

sys.stdin = open("D4_1486_input.txt", "r")


# 비트마스크로 가능한 모든 조합을 따지는 풀이
def ladder():
    com = []
    for i in range(1<<n):
        temp = 0
        for j in range(n):
            if (1<<j) & i:
                temp += heights[j]
        com.append(temp)
    # 조합을 정렬
    com.sort()
    # 순차탐색을 이용하여 b와 가장 가까운 조합을 찾아냄
    for i in range(len(com)-1, 0, -1):
        if com[i] > b:
            continue
        elif com[i] == b:            
            return 0
        else:
            return com[i+1] - b


# 백트래킹을 이용한 빠른 풀이
def ladder2():
    backtracking(0, 0)
    # 백트래킹 결과물들(키의 합이 b보다 큰 조합) 정렬하여 제일 작은것 리턴
    result.sort()
    return result[0] - b

def backtracking(k, cursum):
    if k == n:
        # b보다 작은 값은 의미 없으니 크거나 같은 값만 추가
        if cursum >= b:
            result.append(cursum)
    else:
        # 가지치기: cursum이 b보다 크거나 같아지면 result에 더하고 리턴
        # result에 더하지않고 그냥 돌아가면 result가 비는 경우가 생김
        if cursum >= b:
            result.append(cursum)
            return
        check[k] = 1
        backtracking(k+1, cursum+heights[k])
        check[k] = 0
        backtracking(k+1, cursum)


t = int(input())
for test_case in range(t):    
    n, b = map(int, input().split())
    heights = list(map(int, input().split()))
    check = [0]*n
    result = []
    # print('#' + str(test_case + 1), ladder())
    print('#' + str(test_case + 1), ladder2())