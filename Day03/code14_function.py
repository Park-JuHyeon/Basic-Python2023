# 함수
# 함수정의 - 이건 실행이 아님
def add(x,y):
    result = x + y
    return result   # return이 없으면 아무값도 돌아오지 않음 return을 통해 1029가 val로 돌아감

def sub(x,y):
    result = x - y
    return result

def mul(x,y):
    result = x*y
    return result

def div(x,y):
    result = x/y
    return result

# 함수 호출
val = add(1024, 5) 
print(val)

val = sub(1024, 1000)
print(val)

val = mul(512,2)
print(val)

val = div(108,10)
print(val)

