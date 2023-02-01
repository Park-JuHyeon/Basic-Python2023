## if문 배우자 - 항상 끝에 콜론 : 가 반드시 들어가야함@!!!

name = '주현'
state = '안아픔'

if name == '주현':
    print('진료실에서 담당의사를 만납니다')
    if state == '아픔':
        print('선생님 배가 아파용~')
        print('배 어디가 어떻게 아파요?')
    else:
        print('어디가 아프십니까?')
        print('안아픈데여')
        print('그럼 왜왔음?')

elif name == '다원':
    print('주사실로 갑니다.')
    print('엉덩이 내리세여~')
    
else:
    print("조용히 기다립니다.")




