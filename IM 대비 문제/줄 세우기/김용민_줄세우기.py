N = int(input())
numbers = list(map(int, input().split()))
students = list(range(1, N+1))

order = []
# 반복문
for n in range(N):
    # 현재 order의 길이에서 뽑은 번호를 뺀 위치에 학생을 배치
    order.insert(len(order)-numbers[n], students[n])
# 출력
print(" ".join(list(map(str, order))))
