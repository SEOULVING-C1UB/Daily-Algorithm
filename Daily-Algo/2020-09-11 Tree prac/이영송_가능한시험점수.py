T = int(input())
for t in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    # 숫자들의 합을 저장할 memoization 리스트를 만듭니다.
    # 모든 부분집합의 합에 0이 포함되므로 0인덱스에 0을 만들어둡니다.
    # 또한 memo의 0번째 0 값은 자기 자신을 1회 더해주는 값과 같은 의미를 가집니다.
    memo = [0]
    # memo의 0번째 원소는 방문했으므로 1로 체크해두고
    # numbers의 부분집합의 합의 크기는 전체 합보다 작거나 같으므로
    # visited의 최대 크기를 sum 내장함수로 선언합니다.
    visited = [1] + [0] * sum(numbers)
    # number의 숫자를 하나씩 꺼내가며
    # i 이전의 원소(0:i-1)들로 이루어진 부분집합의 합 리스트에 i번째 숫자를 더해줍니다.
    # memo의 길이만큼 반복하면 i-1번째로 이루어진 모든 부분집합의 합을 구현할 수 있습니다.
    # 그리고 visited에는 해당 i+memo[0~j]까지의 요소가 중복되지 않도록 체크해줍니다.
    for i in numbers:
        for j in range(len(memo)):      # memo의 길이는 i 시행에 따라 늘어납니다.
            if visited[i + memo[j]] == 0:   # i번째 원소와 그 이전의 부분집합의 합이 중복되지 않는다면
                memo.append(i + memo[j])    # 추가하고
                visited[i + memo[j]] = 1    # 방문처리하여 중복을 막습니다.

    print('#{} {}'.format(t, len(memo)))