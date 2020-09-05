import sys

sys.stdin = open("토너먼트카드게임_input.txt", "r")

def winner(nums):
    n = len(nums)   # 현재 카드 배열의 길이
    if n == 1:      # 입력 카드 배열 길이가 1이면 그대로 반환
        return nums[0]  # nums가 [(1,3)] 과 같은 형태이므로 값을 반환하기 위해 nums[0]
    elif n == 2:    # 카드가 두개라면 비교!!
        # 찌가 보를 이기는 상황을 제외하고는 모두 숫자가 크면 승리
        if max(nums[0], nums[1], key=lambda x: x[0])[0] == 3 and min(nums[0], nums[1], key=lambda x: x[0])[0] == 1:
            return min(nums[0], nums[1], key=lambda x: x[0])    # 순번이 아닌 카드 값으로 비교, 값이 같으면 앞에 있는 값이 반환
        else:
            return max(nums[0], nums[1], key=lambda x: x[0])
    else:
        return winner([winner(nums[:(n+1)//2]), winner(nums[(n+1)//2:])])
        # 규칙에 따라 반 갈라서 함수 재호출, ex) winner([(1,1), (2,3)]) 과 같은 형태가 됨
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = list(zip(map(int, input().split()), range(1, n+1)))  
    # zip을 사용해서 각 카드에 번호 매겨주기
    # ex) [(1,1),(3,2),(2,3),(1,4)]
    print('#{} {}'.format(test_case, winner(nums)[1]))