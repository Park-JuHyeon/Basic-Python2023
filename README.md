# study-Python2023
부경대 IoT 파이썬 학습 리포지토리

## 1일차
1. 기본구성
    - Git/Github 설치 및 연동
    - Visual studio code 설치 및 연동
    - Python 설치
2. 파이썬 기본
    - 콘솔 출력
    - 주석

```python
# desc : 콘솔출력 - 주석
print('Hello, python!!') # 콘솔출력 함수
```


## 2일차
1. 파이썬 기본
    - 콘솔출력
    - 변수
    - 자료형
    - 연산자
    
```python
# 변수
val = 1

# 자료형
print(type(val))  # <class 'int'>

# 문자열 포맷팅
pi = 3.141592
print(f'파이는 {pi}입니다.') # pi는 3.141592입니다.
print(f'파이는 {pi:0.2f}입니다.') # 0.2는 소수점 2번째 까지까지 출력하라는 뜻 : 파이는 3.14입니다
print(f'파이는 {pi: 10.3f}입니다.') # 10.3은 앞에 10자리를 띄우고 소수점 3번째 까지 출력 파이는          3.142입니다.

# 연산자
## 문자열 연산
first = 'Hello'
second = 'world!'
print(first + second) # Helloworld
print(first + ' ' + second) # Hello world

## 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7 # 0번째 que의 자리에 7을 대입

print(que) # [7, 2, 3, 4, 5]

que.append(10) # 맨 마지막에 추가하는 것
print(que) # [7, 2, 3, 4, 5, 10]

que.insert(3, 99) # 특정 인덱스에 추가
print(que) # [7, 2, 3, 99, 4, 5, 10]

que.remove(99) # 해당되는 값 삭제
print(que) # [7, 2, 3, 4, 5, 10]


```

## 3일차
1. 파이썬 기본
    - 흐름제어
        - if
        - for
        - while
    - 구구단 프로그램
    - 함수

```python
# 구구단 - 2중 for문
for x in range(2,10):
    print(f'{x}단 시작 ======')
    for y in range(1,10):
        print(f'{x} X {y} = {x*y:>2}', end=' ')  # 출력의 마지막을 스페이스바로 바꿈, 
                                                 #:>2 는 두자리로 만들어서 줄맞춤 하라는 뜻
        #print(x, 'x', y, '=', x*y)
    print()   # 안쪽 for문을 빠져나와서 줄을 바꿔준다.

# 함수
# 함수정의 - 이건 실행이 아님
# 함수만드는 방법 4가지
# 1. 파라미터O 리턴O
# 2. 파라미터O 리턴X
# 3. 파라미터X 리턴O
# 4. 파라미터X 리턴X
def add(x,y):  # 함수종류의 2번째
    result = x + y
    print(result)

def sub(x,y):
    result = x - y
    print(result)

def mul(x,y):
    result = x*y
    print(result)
    
def div(x,y):
    result = x/y
    print(result)
    
def hello():    #()안에 있는 것이 파라미터, 파라미터 없이 리턴안하는것 4번째
    print('Hello~!!')
    
def hello2():  #함수종류의 3번째
    msg = 'Hello, Hello'
    return msg

# 함수 호출
hello()
print(hello2())

add(1024, 5) 
sub(1024, 1000)
mul(512,2)
div(108,10)

# 계산기만드는 code17 다시한번 살펴보기!!!!
# 전역/지역 = 글로벌/로컬 함수
num = 1

for i in range(1, 11):
    num = i * num
    print(f'{i + 1}번')

    if i % 3 == 0:    # 3의 배수이면
        res = '테스트'
        print(res)

print(f'결과 {num}')
print(res)



```
    
# 4일차
1. 파이썬 기본
    - 가상환경 => 패스
    - 객체지향 OOP
    - 패키지, 모듈

```python
# 클래스 생성
class Person:     # 클래스 정의할때는 ()없음 클래스에서는 self가 항상 들어가야함!!!
    # 초기화하는 함수 init
    def __init__(self, name = '홍길동', height = 170 , gender = 'male') -> None:  
    
hong = Person()
hong.run('slow')
print(hong)  # 2. 홍길동 : 이름은 홍길동 성별은 male 출력

# 모듈사용
import math as m   # 클래스로 안된 모듈
import code22_person as p # 우리가 만든 클래스
from code23_car import Car

# 우리가 만든 모듈을 사용해보자
me = p.Person('홍길순', 155, '여성')
print(me)  # '출력: 이름은 홍길순 성별은 여성' 출력.

```
# 5일차 
1. 파이썬 기본
    - 패키지 계속..
    - 입출력 다시
    - 예외처리
    
```python
# random 모듈 사용 (로또 번호 생성기)
import random

# print(random.choice(range(1, 7)))  1 ~ 6까지의 숫자중 랜덤으로 하나

numbers = [i for i in range(1, 46)] # 1~45까지의 리스트
lottery = []

for i in range(6):
    lottery.append(random.choice(numbers))

print(lottery)  # 랜덤으로 번호 6개가 출력됨

# 입출력 : I O 다중입력  <중요함>

# x, y = input('두 영단어를 입력하세요 > ').split()
# print(x)
# print(y)

# 완전 다중입력(개수가 몇개든 상관없음) 매우중요@@!!
inputs = list(map(str, input('단어를 입력하세요 > ').split()))

print(inputs)

inputs = list(map(int, input('정수를 입력하세요 > ').split()))

print(inputs)    # 단어를 입력하세요 > 안녕 난 무명성 지구인이야 ['안녕', '난', '무명성', '지구인이야']
                 # 정수를 입력하세요 > 4 5 6  [4, 5, 6]

# 예외처리 try, except
try:
    x, y = input('두수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:   
    print('계속되나요?')   # 이거 실행뒤 종료됨


```
# 6일차
1. 파이썬 기본
    - 콘솔 출력 보충
    - 객체지향 다시
        - 객체지향 특징
        - 상속, 다중 상속

2. 파이썬 응용
    - 주소록 프로그램 만들기


실행화면


    
    
    
    
    
    
    
    
    
    
    


