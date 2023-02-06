# 콘솔 출력 보충
# 이스케이프 캐릭터(탈출 문자)

# print('1. Hello.\r\nWorld')
print('2. Hello.\nWorld')  # 이걸 권장

print('3.Hello.\n\t World')  # t == tab
print('4.Hello.\n\t\b World') # b == backspave
print('5.Hello.\n\'World\'')  # \' 문자열내에 홑따옴표
print('6.Hello. "World"')  # 이걸 사용하는게 좋음
print('7.Hello. \"World\"')  # 6번과 같은 출력나옴

print('8.Hello. \\ World')  # \를 문자열에 표현 (파이썬에서만 가능)
print('9.Hello\0')   # 널문자 표현

# 문자열 포맷팅 - 구닥다리ver
# %로 포맷코드를 시작
me = '저'
name = '박주현'
age = 20
print('%s는 %s입니다. %d대입니다.'%(me, name, age))

print(f'{254.4454212:.2f}')  # 최신식
print('%4.4f' %(254.112233))  # 구식 %4.4 => 전체자리수.소수점



