C, R = map(int, input().split())
for _ in range(10):
    K = int(input())
    s = [1]
    for i in range(min(C, R) // 2):
        s.append(s[i] + ((C - i * 2) + (R - i * 2)) * 2 - 4)
    for i in range(1, len(s)):
        if K < s[i]:
            line = i - 1
            break
    C, R = C - line * 2, R - line * 2
    cnt = K - s[line]
    if cnt < R:
        print(line + 1, line + 1 + cnt)
    elif R <= cnt < R + C - 1:
        print(line + 1 + K - R, line + R)
    elif R + C - 1 <= cnt < 2 * R + C - 2:
        print(line + 1 + C - 1, R - line - (cnt - (R + C - 2)))
    else:
        print(line + 1 + s[line + 1] - (cnt), line + 1)
