
# 자동차 클래스
class Car:  # 색상이 녹색을 띄는 애들은 모두 클래스이다.
    __number = '54라 9538'  # number에 __가 들어가면 캡슐화가 된다.

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    #클래스 외부에선 변경 안되지만 멤버함수로는 내부를 조작 가능
    def __init__(self, number = '54라 9538') -> None:  # 2번
        self.__number = number
        print('__init__')    # __init__ : 초기화하는것
       

   # def __new__(cls):    # new가 1번째로 실행됨
   #    print('__new__')   # __new__ : 새로운 클래스를 생성하는 것. 근데 잘 안씀.
   #    return super().__new__(cls)   # super = 부모 클래스 상속!

    def __str__(self) -> str:
        return f'제차 번호는 {self.__number} 입니다. '

yourcar = Car('88호 7645')
print(yourcar)
yourcar.__number = '54라 9999'  # 클래스외부에서 접근시 멤버변수에 접근불가
print(yourcar)
print('클래스 내부함수 사용!')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car()
print(mycar)
print(f'제차는요 제네시스고 번호는 {mycar.get_number()} 입니다.' )

mycar.__number = '132거 8874'
print(mycar.get_number())
print(mycar)




