'''
[컨셉]
1) scores 배열에 가능한 점수들을 저장함, 초기값은 다 틀리는 0점.
2) 시험 채점을 생각하면, n번 문제를 채점했을 때 가능한 점수는 (n-1번까지의 점수)에 (n번째 배점)을 더하거나, 더하지 않는 것이다.
   더하지 않는 경우는 이미 scores에 저장되어 있으니, 더하는 경우만 생각해서 temp에 담고, 이를 scores에 붙인 후 중복 값은 제거한다.
* subset sum을 이리저리 변형해보다가 runtime error을 수없이 마주하고 DP로 전략 변경.
'''

T = int(input())
for t in range(T) :
    N = int(input())                        # N개의 문제
    li = list(map(int, input().split()))    # 각 문제의 배점을 담을 배열
    scores = [0]                            # 가능한 점수가 담길 배열
    
    for num in li :                         # 각 문제에 대하여
        temp = []                           
        for score in scores :               # 이전 문제까지 채점했을 때 가능한 점수들에 대하여
            temp.append(score + num)        # 이번 문제를 맞췄을 때의 점수를 추가한다. (틀린 경우는 이미 scores에 있음)
        scores.extend(temp)                 # 이번 문제를 맞췄을 경우를 scores와 합쳐주고
        scores = list(set(scores))          # 중복 값은 제거한다.
    print('#{} {}' .format(t+1, len(scores)))