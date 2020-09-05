def turn():
    # 원형 큐라고 생각하면 아래의 한 줄로 표현 가능  
    return nums[m%n]
    

T = int(input())
for test_case in range(T):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print('#' + str(test_case + 1), turn())
