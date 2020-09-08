def sol(h, i):
    '''
    recursive function that check whether 'h' is bigger than 'b'.
    :param h : sum of people's height:
    :param i : index of list 'l'
    :return:
    '''
    global ans
    # end condition
    if h >= b:
        ans = min(ans, h)
        return
    
    # recursive
    if i <= n - 1:
        sol(h, i + 1) # don't contain l[i]
        sol(h + l[i], i + 1) # contain l[i]


for t in range(int(input())):
    ans = 1 << 32
    n, b = map(int, input().split())
    l = list(map(int, input().split()))
    sol(0, 0)
    print(f'#{t + 1}', ans - b)

# Recursion is faster way than the answer below. In the worst case,
# it takes same time. You can also solve by stack.

# from itertools import combinations as coms
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     H = list(map(int, input().split()))
#     H.sort()
#     ans = sum(H)
#     for i in range(1, N + 1):
#         for com in coms(H, i):
#             if B <= sum(com) < ans:
#                 ans = sum(com)
#     print(f'#{tc} {ans - B}')
