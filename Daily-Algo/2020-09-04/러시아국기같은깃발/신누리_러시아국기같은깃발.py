'''
[컨셉]
1) 문제를 N개의 열을 세가지 색이 나눠 갖는 것으로 단순화할 수 있다.
   - 즉, 0 + i / i+1 ~ j / j ~ N-1 이렇게 열을 나누고, 차례대로 W, B, R로 채우면 된다.
2) 각 열에서 몇 개를 다시 칠해야하는지 매번 list를 순회하려면 비효율적이라서,
   처음에 input을 받을 때 행 별로 각 색이 몇칸 있는지를 저장한다.
'''

T = int(input())
for t in range(T) :
    N, M = map(int, input().split())
    # colors라는 2차원 배열에 각 행별로 W, B, C가 각각 몇개 있는지 저장된다. 즉 3*N 배열.
    colors = []
    for i in range(N) :
        row = list(input())
        temp = []
        temp.append(row.count('W'))
        temp.append(row.count('B'))
        temp.append(M-temp[0]-temp[1])
        colors.append(temp)
    
    # mini에는 결과값 저장. 색을 전부 바꾸는 경우인 M*N이라는 최댓값으로 초기화.
    mini = M*N
    
    # (0, i) (i+1, j) (j+1, N-1)로 구역을 나누는 과정이다.
    for i in range(0, N-2) :            # 0 <= i <= N-3
        for j in range(i+1, N-1) :      # i+1 <= j <= N-2
            
            # 구역을 나누면, 몇칸을 바꿔야 하는지 센다.
            cnt = M*N
            for a in range(N) :         # colors를 순회하며
                if a <= i :             # 색을 W로 칠해야 할 때
                    cnt -= colors[a][0]
                elif i < a <= j :
                    cnt -= colors[a][1] # 색을 B로 칠해야 할 때
                else :
                    cnt -= colors[a][2] # 색을 R로 칠해야 할 때
            if cnt < mini :             # 최솟값이라면 갱신
                mini = cnt
    print('#{} {}' .format(t+1, mini))
