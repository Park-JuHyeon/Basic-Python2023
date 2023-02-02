# 클래스 생성
class Person:    
   # pass   person에 넣을게딱히없을때 pass를 사용
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    def walk(self):   # 클래스에서 self는 항상 들어가야한다 무조건!
        print('걷습니다')

    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}이(가) 빨리 뜁니다!!')
        else:
            print(f'{self.name}이(가) 천천히 뜁니다.')

    def stop(self):
        print('멈춥니다.')

JuHyeon = Person()   # 이러한 형태의 객체를 instance라고 함.
JuHyeon.name = '박주현'
JuHyeon.height = '170'
JuHyeon.gender = 'male'
JuHyeon.blood_type = 'A'

print(f'{JuHyeon.name}의 혈액형은 {JuHyeon.blood_type}형 입니다.')

JuHyeon.run('Fast')
JuHyeon.stop()





