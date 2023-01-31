# 연산자
# 할당연산 assignment
# 2 = 1 (x)

val = 1

# equal 연산자 : 두개가 같은가?
print(1 == 1)

# 사칙연산
print(1 + 1)
print(1 - 1)
print(10 * 10)
print(1024 / 2) # 소수나누기
print(1024 // 2) # 정수나누기
print(6 // 3) 
print(6 % 3) # 나머지 => 뒤의값의 배수

# print(6 / 0) = 에러남.
# print(6 // 0)

print(2 ** 10)  # 제곱을 출력하는 방법 2의 10승

# 문자열 연산
first = 'Hello'
second = 'world!'
print(first + second)
print(first + ' ' + second)

print(first * 4)
# print(first - second) 존재하지않음. 오류남

# 문자열 길이
print(len(first))
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
#print(first[5]) # 인덱스 에러

# 파이썬에 인덱스 찾는 특이한 방법!
print(first[-1])
print(first[-2])
print(first[-3])
print(first[-4])
print(first[-5])

# 리스트 자르기
current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0 : 4])
print(current[5 : 7])
print(current[8 : 10])
print(current[11 : 13])
print(current[14 : 16])
print(current[17 : ])

print(current[-19 : -15])

# 리스트 연산
que = [1, 2, 3, 4, 5]
que[0] = 7

print(que)

que.append(10) # 맨 마지막에 추가하는 것
print(que)

que.insert(3, 99) # 특정 인덱스에 추가
print(que)

que.remove(99) # 해당되는 값 삭제
print(que)

# tup = (1,2,3,4,5) 튜플에서는 값을 할당할 수 없다.

# 문자열 == 문자 리스트
title = 'python'
print(title)

#title[0] = 'P' # 문자열에서는 값변경 안됨.
print('P' + title[1:]) 

# 일반적인 문자열 리스트
text = ['p', 'y', 't', 'h', 'o', 'n']
print(text)
text[0] = 'P'
print(text)

# 구식 문자열 포멧팅
print("I'm so happy {0} you, {1}!!".format(2, 'hey'))

#최신식 문자열 포멧팅
preword = 3
sayHello = 'Hey'
print(f"I'm so happy {preword} you, {sayHello}!!")

pi = 3.141592
print(f'파이는 {pi}입니다.')
print(f'파이는 {pi:0.2f}입니다.') # 0.2는 소수점 2번째 까지까지 출력하라는 뜻
print(f'파이는 {pi: 10.3f}입니다.') # 10.3은 앞에 10자리를 띄우고 소수점 3번째 까지 출력

# 문자열을 특정문자로 자르기
full_name = 'Park JU HYeon'
vals = full_name.split() # 공백으로(스페이스로) 자르기
print(type(vals))
print(vals)

vals = full_name.split('.') # .단위로 자르기(split)
print(vals)

print(full_name.replace('Park', 'Ashely')) # 단어를 대체하기(replace)

# 문자열 공백 없애기
hi = '          Hello~ Bye~          '
print(hi.lstrip() + '|') # '|'는 파이프라고 부른다
print(hi.rstrip() + '|')
print(hi.strip() + '|')

# 문자열에서 값을 찾기
print(full_name.index('J'))
# print(full_name.index('Z')) 없는 문자 찾으면 오류남

print(full_name.find('Z')) # 찾는 값이 없으면 -1이 출력된다.
print(full_name.find('J'))

# 찾는 단어의 개수를 알려주는 count()
print(full_name.count('U'))

# 모든 단어를 대문자 또는 소문자로 변경
print(full_name.upper())
print(full_name.lower())

# 연산자 우선순위
print(3 + 4 * 2)
print((3 + 4) * 2)







