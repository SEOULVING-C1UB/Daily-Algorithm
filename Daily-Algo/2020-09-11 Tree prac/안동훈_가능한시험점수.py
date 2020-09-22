import sys
sys.stdin = open('가능한시험점수_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    answer = 0
    n = int(input())
    scores = list(map(int,input().split()))
    possible = [0]*(sum(scores)+1) # 가능한 점수군
    possible[0] = 1
    max = 0
    idx = 0
    while True: # 인덱스를 뒤에서부터 앞으로 하면 재미있다.
        if idx == n:
            break
        for i in range(max, -1, -1):
            if possible[i] == 1:
                possible[i+scores[idx]] = 1
        max += scores[idx]
        idx += 1

    # 가능한 시험 점수 체크
    for i in range(len(possible)):
        if possible[i] == 1:
            answer += 1
    print("#{0} {1}".format(test_case, answer))