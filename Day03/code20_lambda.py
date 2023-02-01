# 람다함수   : 한번쓰고 버리는 함수를 의미함
def add(x, y):
    return x + y

print(add(7, 4))

#람다 함수로 쓰면
print((lambda x, y: x+y)(7,4))

# 지금은 쓰지말자!! 복잡하니까~