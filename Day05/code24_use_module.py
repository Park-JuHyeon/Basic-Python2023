# random 모듈 사용 (로또 번호 생성기)
import random

# print(random.choice(range(1, 7)))  1 ~ 6까지의 숫자중 랜덤으로 하나

numbers = [i for i in range(1, 46)] # 1~45까지의 리스트
lottery = []

for i in range(6):
    lottery.append(random.choice(numbers))

print(lottery)






