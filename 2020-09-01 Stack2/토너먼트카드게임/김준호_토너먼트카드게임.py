import sys

sys.stdin = open("토너먼트카드게임_input.txt", "r")

def winner(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    elif n == 2:
        if max(nums[0], nums[1], key=lambda x: x[0])[0] == 3 and min(nums[0], nums[1], key=lambda x: x[0])[0] == 1:
            return min(nums[0], nums[1], key=lambda x: x[0])
        else:
            return max(nums[0], nums[1], key=lambda x: x[0])
    else:
        return winner([winner(nums[:(n+1)//2]), winner(nums[(n+1)//2:])])
        
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    nums = list(zip(map(int, input().split()), range(1, n+1)))

    print('#{} {}'.format(test_case, winner(nums)[1]))