for t in range(1,11):
    N = int(input())
    tmp = [list(input().split()) for _ in range(N)]

    # 주어지는 트리가 오름차순으로 정렬된 완전 이진 트리 형식이므로
    # 이진 탐색을 위한 정렬 리스트를 따로 생성할 필요가 없음

    # 각 노드에 담긴 데이터를 저장해 줄 alphabet 배열을 선언
    # 노드의 번호 = alphabet 인덱스로 연결
    alphabet = [0]*(N+1)
    for i in range(N):
        idx = int(tmp[i][0])
        alphabet[idx] = tmp[i][1]

    # 재귀를 사용한 풀이
    # 글자를 순서대로 담을 answer 리스트 새로 생성
    answer = []
    def search(n):
        if n > N:       # n==N 까지 데이터가 존재하므로 base 조건 설정
            return
        else:
            search(2*n)             # 왼쪽 자식 노드
            answer.append(alphabet[n])  # 방문 시 읽어 올 데이터, n은 인덱스에 해당
            search(2*n+1)           # 오른쪽 자식 노드
    # 1부터 시작
    search(1)
    print('#{} {}'.format(t,''.join(answer)))
