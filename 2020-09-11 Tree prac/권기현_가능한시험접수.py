import sys
sys.stdin = open('3752.txt')

total_tc = int(input())


for tc in range (1, total_tc+1):
    N = int(input())
    input_scores = list(map(int, input().split()))

    visit = [0] * (sum(input_scores)+1)
    possible_scores = [0]

    for val in input_scores:
        for i in range(len(possible_scores)):
            if visit[possible_scores[i] + val] : continue
            visit[possible_scores[i] + val] = 1
            possible_scores.append(possible_scores[i] + val)

    print("#%d %d"%(tc, len(possible_scores)))

