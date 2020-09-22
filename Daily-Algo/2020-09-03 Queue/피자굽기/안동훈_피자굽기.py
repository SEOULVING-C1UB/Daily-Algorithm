import sys
sys.stdin = open('피자굽기_input.txt')

# 7/10 맞은 문제입니다. 실습으로 배워야겠네요..
T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    queue = []
    for idx, cheeze in enumerate(pizza): # enumerate를 이용하여 피자의 번호와 현재 치즈 양을 받는다.
        queue.append([idx+1, cheeze])

    while len(queue) != 1:
        # 화덕에 피자가 하나만 남으면 중지
        for i in range(len(queue)):
            idx, remain_cheeze = queue.pop(0)
            remain_cheeze = remain_cheeze // 2
            # 치즈가 다 녹지 않았으면 다시 화덕에 넣는다.
            if remain_cheeze != 0:
                queue.append([idx, remain_cheeze])
            else:
                break

    answer = queue[0][0]
    print("#{0} {1}".format(test_case, answer))