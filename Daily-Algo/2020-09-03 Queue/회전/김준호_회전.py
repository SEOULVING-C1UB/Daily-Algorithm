import sys

sys.stdin = open("회전_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))
    for _ in range(m):
        num_list.append(num_list.pop(0))
    print('#{} {}'.format(test_case, num_list[0]))