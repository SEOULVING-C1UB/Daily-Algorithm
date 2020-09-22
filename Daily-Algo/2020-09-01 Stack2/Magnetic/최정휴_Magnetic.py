for i in range(1,11):
    n = int(input())
    lst = []
    ans = 0
    for _ in range(100):
        lst.append(input().replace(" ",""))
        # split 없이 받았기 때문에 공백까지 문자열에 포함되었었다.. 조심좀 하자..
    for j in range(100):
        now = ""
        # 세로로 바라본 현재 열 만들기.
        for k in range(100):
            now += lst[k][j]
        # 만들어진 현재 열에서 공백을 의미하는 0은 replace로 전부 제거
        # 또한 위쪽의 s극(2), 아래쪽의 n극(1)은 교착 상태없이 테이블 밑으로 떨어지므로 strip을 이용하여 제거
        now = now.replace("0","").lstrip("2").rstrip("1")
        # 나머지 자성체들에 대해 n극 다음 s극이 오는 한 쌍을 만나면 교착상태의 갯수(ans)를 1증가
        for k in range(len(now)-1):
            if now[k] == '1' and now[k+1]=="2":
                ans += 1
    print(f'#{i} {ans}')