def test(a, res):
    if a[0] != '+' and a[0] != '-' and a[0] != '*' and a[0] != '/' and a[0] != '.': # 숫자일 경우
        res += [a[0]]
        a.pop(0)
        test(a, res)
    elif a[0] == '+' or a[0] == '-' or a[0] == '*' or a[0] == '/': # + - * / 일 경우
        if len(res) >= 2:
            if a[0] == '+':
                res += [int(res.pop(-2)) + int(res.pop(-1))]
                a.pop(0)
                test(a, res)
            elif a[0] == '-':
                res += [int(res.pop(-2)) - int(res.pop(-1))]
                a.pop(0)
                test(a, res)
            elif a[0] == '*':
                res += [int(res.pop(-2)) * int(res.pop(-1))]
                a.pop(0)
                test(a, res)
            elif a[0] == '/':
                res += [int(res.pop(-2)) // int(res.pop(-1))]
                a.pop(0)
                test(a, res)
        else: # len(res)가 2보다 작으면 숫자가 한 개 이하라는 뜻이므로 + - * / 을 사용할 수 없음
            return 'error'
    elif a[0] == '.':
        if len(res) == 1 and len(a) == 1:
            for _ in res:
                return _
        else: # .이 나오고 len(res)에서 하나만 뽑으면 끝이고 a에도 더 이상 값이 있으면 안 된다
            return 'error'


T = int(input())

for tc in range(1,1+T):
    a = list(map(str,input().split()))

    res = []

    test(a,res)

    print('#{} {}'.format(tc,test(a,res)))