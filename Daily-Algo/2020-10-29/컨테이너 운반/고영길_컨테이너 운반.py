# Starting with heaviest cargo,
# make sure that each cargo can be transported by each truck starting with largest truck.

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    answer = 0
    for i in range(M - 1, -1, -1):
        try:
            while trucks[i] < weights[-1]:
                weights.pop()
            answer += weights.pop()
        except IndexError: # no more cargo can be transported by left truck
            break
    print('#{} {}'.format(tc, answer))