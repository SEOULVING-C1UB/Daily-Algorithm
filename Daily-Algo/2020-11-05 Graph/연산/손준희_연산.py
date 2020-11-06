from collections import deque


for TC in range(int(input())):
    N, M = map(int, input().split())
    already = [0] * 1000001  # 이미 확인한 score라면 더는 살펴볼 필요가 없다.
    already[1] = already[N] = 1
    stack = deque([[N, 0, -1]])
    flag = 1
    while flag and stack:
        score, step, oper = stack.popleft()     # 점수, 연산횟수, 연산자
        for i in range(4):
            if i == 0:  # +1 연산
                if oper == 1:   # 직전에 -1 했는데 +1 할 이유 없음
                    continue
                new_score = score + 1
                if score == M:  # 목표로 한 점수라면
                    min_step = step
                    flag = 0
                    break   # 브레이크
                if score < M and 0 < new_score < 1000001:   # M보다 큰 점수라면 굳이 고려할 필요 없다.
                    if not already[new_score]:  # 한번도 나오지 않은 score인 경우에만
                        stack.append([new_score, step + 1, i])  # stack에 추가한다.
                        already[new_score] = 1
            elif i == 1:    # -1 연산
                if oper == 0:   # 직전에 +1 했는데 -1 할 이유 없음
                    continue
                new_score = score - 1
                if score == M:
                    min_step = step
                    flag = 0
                    break
                if 0 < new_score:
                    if not already[new_score]:
                        stack.append([new_score, step + 1, i])
                        already[new_score] = 1
            elif i == 2:    # *2 연산
                new_score = score * 2
                if score == M:
                    min_step = step
                    flag = 0
                    break
                if score < M and 0 < new_score < 1000001:   # M보다 큰 점수라면 굳이 곱할 이유가 없다.
                    if not already[new_score]:
                        stack.append([new_score, step + 1, i])
                        already[new_score] = 1
            elif i == 3:    # -10 연산
                new_score = score - 10
                if score == M:
                    min_step = step
                    flag = 0
                    break
                if 0 < new_score:
                    if not already[new_score]:
                        stack.append([new_score, step + 1, i])
                        already[new_score] = 1
    print('#{} {}'.format(TC + 1, min_step))
