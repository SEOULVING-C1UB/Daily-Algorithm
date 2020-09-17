import sys
sys.stdin = open('scores_input.txt', 'r')

# def powerset(n, k):
#     if n == k:
#         scoreset.add(sum(score))
#     else:
#         score.append(scores[k])
#         powerset(n, k+1)
#         score.remove(scores[k])
#         powerset(n, k+1)

for TC in range(int(input())):
    N = int(input())
    scores = list(map(int, input().split()))
    score_value = [0] * (sum(scores) + 1)   # scores의 모든 합 이하의 행렬 생성
    score_value[0] = 1                      # 그 후 메모이 어쩌구 사용할 예정
    check = [0]                         # 이것은 확인할 합계값들의 list
    for score in scores:                    # 모든 score에 대해서 확인하면 된다
        for i in range(len(check)):         # score를 갖고 시작할 때 현재 check의 길이만큼만 for문을 돈다
            if not score_value[score + check[i]]:   # 계산한 값이 한번도 나왔던 값이 아니면
                score_value[score + check[i]] = 1   # 나온 것으로 체크하고
                check.append(score + check[i])      # 해당 점수를 check에 넣는다
    print('#{} {}'.format(TC + 1, sum(score_value)))

    # 시간초과
    # for TC in range(int(input())):
    #     N = int(input())
    #     scores = list(map(int, input().split()))
    #     scorelist = [0]
    #     for score in scores:
    #         for i in range(len(scorelist)):
    #             if score + scorelist[i] not in scorelist:
    #                 scorelist.append(score + scorelist[i])
    #     print('#{} {}'.format(TC + 1, len(scorelist)))