import sys
sys.stdin = open("5097_회전.txt")

t = int(input())

for i in range(1,t+1):
    n, m = map(int,input().split())
    lst = list(map(int,input().split()))
    print('#{} {}'.format(i, lst[m%n]))
    # 숫자들이 돈다고 생각하지말고 인덱스가 밀린다고 생각하면 편함
    # 원소가 n개 주기는 n. 따라서 m을 n으로 나눈 나머지만큼만 인덱스를 뒤로 밀어주면 끝.