T = 10

def cal(s): #계산
    n = 1   # 인덱스 0은 숫자 1부터 연산자 가능
    while True: # 앞부터 탐색
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return int(s[0])
        if s[n] == '+':
            return int(s[:n]) + cal(s[n+1:])    # 연산자 앞부분은 숫자로 뒤는 재귀
        elif s[n] == '*':   
            res = int(s[:n])    # 곱셈 결과를 저장할 값
            temp = s[n+1:]      # 아직 모르는 뒷부분
            i = 0
            while temp[i] != '+':   # 곱셈이 거듭해서 나올 수 있으므로 더하기 연산자 나오기 전까지
                if temp[i] == '*':  
                    res *= int(temp[:i])    
                    temp = temp[i+1:]
                    i = 0
                    continue
                if i == len(temp) - 1:  # 마지막이라면
                    i += 1
                    break
                i += 1
            res *= int(temp[:i])    
            return res + cal(temp[i+1:])
        if len(s)-1 == n:   # 마지막까지 탐색, 전부 다 숫자
            return int(s)
        n += 1
def comp(s):    # 괄호 제거
    start = 0
    end = 0
    for i, c in enumerate(s):
        if c == '(':
            start = i
        elif c == ')':
            end = i
            if end == len(s) - 1:   # 전체를 감싸는 괄호일때
                return cal(s[1:-1])
            return comp(s[:start] + str(cal(s[start + 1:end])) + s[end+1:])
            # 괄호 안은 계산하고 괄호 제거한 전체를 재귀
    return cal(s)   # 괄호가 없다면

for test_case in range(1, T + 1):
    n = int(input())
    s = input()
    print(f'#{test_case} {comp(s)}')