from collections import deque

for tc in range(int(input())):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    q = deque([[0, 0]])
    result = prices[-1]
    while q:
        month, total_price = q.popleft()
        if total_price > result:
            continue
        if month == 12:
            if result > total_price:
                result = total_price
        else:
            if month < 10 and prices[2] < prices[1] * 3 and prices[2] < prices[0] * sum(plan[month:month + 3]):
                q.append([month + 3, total_price + prices[2]])

            if prices[1] < prices[0] * plan[month]:
                q.append([month + 1, total_price + prices[1]])
            else:
                q.append([month + 1, total_price + prices[0] * plan[month]])

    print("#{} {}".format(tc + 1, result))
