def check(item, res, a):
    if len(a) == 0: # 다 뽑아내면 res를 리턴 함
        return res
    else:
        if a[0] == '(' or a[0] == ')' or a[0] == '+' or a[0] == '*': # 주어진 테스트 케이스에서 숫자가 아니면
            if a[0] == '+' and item[-1] == '*': # + 와 *가 만날 경우
                res += [item.pop()]
                check(item, res, a)
            elif a[0] == ')': # )일 경우, ( 나올 때 까지 다 뽑아냄
                res += [item.pop()]
                if item[-1] == '(': # ( 일 경우
                    item.pop()
                    a.pop(0)
                    check(item, res, a)
                elif item[-1] != '(':
                    check(item, res, a)
            else: # tc에서 뽑은 값이 숫자일 경우, item에 그냥 추가
                item += [a[0]]
                a.pop(0)
                check(item, res, a)

        else:
            res += a[0]
            a.pop(0)
            check(item, res, a)


for tc in range(1,11):
    t=int(input()) # tc의 길이
    a=list(str(input())) # tc

    item = []

    res = [] # 숫자

    cnt = []

    check(item, res, a)

    for w in check(item, res, a):
        if w != '+' and w != '*':
            cnt += [w]
        elif w == '+':
            cnt_plus = [int(cnt[-2]) + int(cnt[-1])]
            cnt.pop()
            cnt.pop()
            cnt += cnt_plus

        elif w == '*':
            cnt_multi = [int(cnt[-2]) * int(cnt[-1])]
            cnt.pop()
            cnt.pop()
            cnt += cnt_multi


    print('#{} {}'.format(tc, cnt[0]))