'''
<기본컨셉>
1) 무늬별 리스트를 따로만들어 카드를 저장
2) 모두 저장 후 중복을 확인하기 위해 set을 이용하여 배열의 길이 비교
3) 각 리스트에 저장된 카드의 갯수를 13에서 빼면 정답

<주의사항>
1) 카드하나의 표현이 S03 과 같이 무조건 길이 3이라 길이로 잘라서 풀었는데 만약 0포함 안시켜준다면 조심해야겠다
'''


t = int(input())

for i in range(1, t+1):
    cards = input()
    card_list = {                                                       # 무늬별 카드 리스트 생성
        'S' : [],
        'D' : [],
        'H' : [],
        'C' : []
    }
    for j in range(len(cards)//3):                                      # 카드 하나당 길이3 짜리 인풋이므로 //3 만큼만 반복하면 됨
        card_list[f'{cards[0+j*3:1+j*3]}'].append(cards[1+j*3:3+j*3])   # f스트링을 이용 첫 글자에 해당하는 리스트에 무늬를 제외한 숫자를 append
    for j in card_list:                                                 # 각 카드 리스트에 대하여
        if len(card_list[j]) != len(set(card_list[j])):                 # 중복 제거한 결과와 원본의 길이가 다르면
            print(f'#{i} ERROR')                                        # 에러 출력
            break
    else:
        print(f'#{i}',end=" ")
        for j in card_list:
            print(13-len(card_list[j]),end=" ")                         # 각 카드리스트의 길이를 13에서 뺀 것이 정답
        print("",end="\n")
