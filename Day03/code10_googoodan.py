# 구구단을 외자
for x in range(2,10):
    print(f'{x}단 시작 ======')
    for y in range(1,10):
        print(f'{x} X {y} = {x*y:>2}', end=' ')  # 출력의 마지막을 스페이스바로 바꿈, 
                                                 #:>2 는 두자리로 만들어서 줄맞춤 하라는 뜻
        #print(x, 'x', y, '=', x*y)
    print()   # 안쪽 for문을 빠져나와서 줄을 바꿔준다.




