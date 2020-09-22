# Sometimes, loop is better than recursion.

for tc in range(1, int(input()) + 1):
    N = int(input())
    points = list(map(int, input().split()))
    scores = set([0])

    # Add points[idx] at score in scores
    for point in points:
        scores.update(set([score + point for score in scores]))

    print('#{} {}'.format(tc, len(scores)))

    
# I realized that the way to check if the score alreay exist in 'list' with the 'boolean list' is faster
# than the way to check for duplicates through 'set'
    scores2 = set([0])
    cnt = 1  # bcuz of 0 point, count start from 1
    # Through use 'cnt', we can skip the process which count the length of 'scores'
    able_score = [False] * (sum(points) + 1)
    for point in points:
        tmp = set()
        for score in scores2:
            if not able_score[score + point]:
                able_score[score + point] = 1
                tmp.add(score + point)
                cnt += 1
        scores2.update(tmp)
