# 매개변수 개수가 일정치 않은경우
def add(*args):   # *args는 값을 여러개받을수있는 변수?
    result = 0
    for i in args:
        result += i
    
    return result

print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6,7,8,9,10))


