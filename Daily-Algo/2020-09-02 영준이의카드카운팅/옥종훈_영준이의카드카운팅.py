import sys

sys.stdin = open("D2_4881_input.txt", "r")

def listsum(n):    
    result = 10000000000    
    # n! 만큼의 순열을 생성해서 perm_list에 저장해줌
    perm(n, 0)    
    for i in range(len(perm_list)):
        temp = 0
        for j in range(n):
            # 서로 다른 위치를 나타내는 인덱스 값을 이용하여 가능한 모든 합 도출
            temp += numbers[j][perm_list[i][j]]
        if temp < result:
            result = temp
    return result

# 가지치기를 도입하지 않았을 때: 시간초과 발생
def perm(n, k):    
    if k == n:
        # 단순히 arr를 더해주면 shallow copy이므로 perm_list의 모든 원소가 같아짐
        perm_list.append(arr[:])
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)            
            arr[k], arr[i] = arr[i], arr[k]

# 모든 경우에 대해 계산하지말고 가지치기 도입
def perm2(n, k, curmin):        
    # 가지치기: 앞부분을 더해봤을때 현재 최저값보다 크면 Stop
    temp = 0
    for i in range(k):
        temp += numbers[i][arr[i]]
    if temp > curmin:
        return curmin

    if k == n:        
        # 마지막에 도달한 상황이면 앞서 계산한 temp를 반환
        # 이 경우 temp는 해당 순열을 따라 배열의 수를 모두 더한 합이 됨
        return temp
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            temp = perm2(n, k+1, curmin)            
            # 현재 최솟값 curmin보다 아래에서 올라온 값이 더 작으면 변경
            if curmin > temp:
                curmin = temp
            arr[k], arr[i] = arr[i], arr[k]
    return curmin


# 더 효율적인 가지치기
def perm3(n, k, cursum):
    global ans
    if ans < cursum:
        return
    if k == n:
        if ans > cursum:
            ans = cursum
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm3(n, k+1, cursum + numbers[k][arr[k]])
            arr[k], arr[i] = arr[i], arr[k]


t = int(input())
for test_case in range(t):
    total = 0
    n = int(input())
    ans = 100000000
    numbers = [list(map(int, input().split())) for _ in range(n)]
    # arr = [i for i in range(n)]
    # perm_list =[]
    # print('#' + str(test_case + 1), listsum(n))       
    # print('#' + str(test_case + 1), perm2(n, 0, 10000000))
    perm3(n, 0, 0)
    print('#' + str(test_case + 1), ans)
