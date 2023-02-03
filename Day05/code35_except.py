# 예외처리(ZeroDivisionError) = 작동은 하지만 예외적으로 오류가나는 부분이 생김
def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:
    x, y = input('두수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:   
    print('계속되나요?')   # 이거 실행뒤 종료됨

# 원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지 마세요')
#     exit()

print('테스트 시작')
try:
    print(div(x,y))
except ZeroDivisionError as e:
    print('0으로 나누면 안되요!')
except Exception as e:  # Exception의 예외처리는 항상 맨 마지막에 처리해야한다. [이것만 써도됨.]
    print(e)
finally:    # 어떡하든 일을 계속하게 해주는 것
    print('계산은 계속됩니다!!!')

print(add(x,y))
print(mul(x,y))





