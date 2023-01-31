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
