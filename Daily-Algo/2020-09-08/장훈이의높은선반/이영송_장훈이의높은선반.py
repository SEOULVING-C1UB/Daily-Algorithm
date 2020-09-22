T = int(input())
for t in range(1,T+1):
    N,B = map(int,input().split())          # 입력값
    height = list(map(int,input().split())) # 입력값

    min_val = 0xfffff                # 최소값 설정

    def subsum(n,k,cursum):
        global min_val
        if cursum >= B and cursum < min_val:    # 가지치기, 부분집합의 합이 B보다 크거나 같으면 return
            min_val = cursum                    # min_val을 매개로 키의 합이 B보다 크거나 같은 것 중에서 최소값 구하기
            return
        if n == k:
            if cursum < B:                      # 모든 부분집합을 구하고 합이 B보다 작으면 return
                return
            else:
                min_val = min(cursum, min_val)  # 모든 부분집합을 구하고 min_val와 비교
        else:
            subsum(n,k+1,cursum+height[k])      # height의 k번째 원소를 더하는 것으로 시작
            subsum(n, k + 1, cursum)            # height의 k번쨰 포함하지 않고 다음으로 넘김

    subsum(N,0,0)
    print('#{} {}'.format(t,min_val-B))