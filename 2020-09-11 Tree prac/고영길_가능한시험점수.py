# Sometimes, loop is better than recursion.

for tc in range(1, int(input()) + 1):
    N = int(input())
    points = list(map(int, input().split()))
    scores = set([0])

    # Add points[idx] at score in scores
    for point in points:
        scores.update(set([score + point for score in scores]))

    print('#{} {}'.format(tc, len(scores)))
