# 클래스 생성
class Person:     # 클래스 정의할때는 ()없음
   # pass   person에 넣을게딱히없을때 pass를 사용
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    # 1. 생성자 추가
    # def __init__(self):
    #    self.name = '홍길동'
    #   self.height = '170'
    #    self.gender = 'male'
    #    self.blood_type = 'ABO'

    def __init__(self, name = '홍길동', height = 170 , gender = 'male') -> None:  # 초기화하는 함수 init
        self.name = name
        self.height = height
        self.gender = gender


    def walk(self):   # 클래스에서 self는 항상 들어가야한다 무조건!
        print(f'{self.name}이(가) 걷습니다')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print(f'{self.name}이(가) 멈춥니다.')

     # 2. 생성자 외 매직메서드(펑션) 
    def __str__(self) -> str:
        return f'출력 : 이름은 {self.name}, 성별은 {self.gender}'

JuHyeon = Person('박주현', 170, 'male')   # 이러한 형태의 객체생성: instance라고 함. 클래스를 사용할때는 ()존재함
#JuHyeon.name = '박주현'
#JuHyeon.height = '170'
#JuHyeon.gender = 'male'
#JuHyeon.blood_type = 'A'

print(f'{JuHyeon.name}의 혈액형은 {JuHyeon.blood_type}형 입니다.')

JuHyeon.run('Fast')
JuHyeon.stop()
print(JuHyeon) # 1. 박주현

# 1.초기화 후에 객체생성
hong = Person()
hong.run('slow')
print(hong)  # 2. 홍길동

print('======================')
# 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'female')
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely) # 3. 애슐리









