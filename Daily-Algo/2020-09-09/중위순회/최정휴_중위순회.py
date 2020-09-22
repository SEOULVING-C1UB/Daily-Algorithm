'''
<문제해결>
1) 주어진 입력을 리스트로 받아 2차원 리스트를 생성
2) 중위순회 함수를 작성한다
3) 해당함수는 좌측자식이 있으면 자식을 재귀호출하고 없으면 넘어간다
4) 좌측자식 확인후 자신을 정답에 집어넣고 우측자식을 확인한다.
5) 우측자식이 있으면 재귀호출하고 없으면 리턴한다

<추가사항>
1) 수업시간에 해주신게 잘 이해 안되서 다르게 한거 같은데.. 다른사람들꺼 보고 공부해야지
2) 입력에 문자가 섞여있어 map으로 int받으면 안됨
3) 그래서 중간중간 int빼먹으면 오류 잘 남
'''
def joong(v):
    try:
        joong(int(tree[v][2]))              # 인풋의 3번째 값이 왼쪽자식
    except:                                 # 왼쪽자식 없으면 pass
        pass
    ans.append(tree[v][1])                  # 왼쪽자식 봤으니 자신을 정답에 추가
    try:
        joong(int(tree[v][3]))              # 인풋의 4번째 값이 오른쪽 자식
    except:
        return                              # 오른쪽자식 없으면 리턴

for i in range(1, 11):
    n = int(input())
    tree = [0]                              # 인덱스 조정 귀찮으니 처음에 0 집어넣어 해결
    for _ in range(n):
        tree.append(list(input().split()))
    visited = [0]*(n+1)                     # 만들어 놓고보니 쓸데없네
    ans = []
    joong(1)
    print('#{} {}'.format(i,"".join(ans)))