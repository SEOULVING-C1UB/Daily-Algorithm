'''
[풀이]
- 먼저 중위순회로 1 ~ N까지 뽑아봤더니 그냥 단어답(?)이 나오는 순서였다
- 그래서 input에서 숫자가 가지는 value값만 저장하는 딕셔너리를 만들어서 
후위 표기식으로 그 숫자에 맞는 알파벳이 나오도록 했음
'''

def inOrder(v):
    global tree
    global result

    if v>N:
        return
    else:
        inOrder(v*2)
        result += tree[v]
        # print(tree[v], end='')
        inOrder(v*2+1)

for tc in range(1, 11):
    N = int(input())

    tree = {}
    for i in range(N):

        tmp = list(map(str, input().split()))
        tree[i+1] = tmp[1]

    result = ''
    inOrder(1)
    print('#{} {}'.format(tc, result))