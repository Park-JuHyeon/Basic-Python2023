# while 문
hit = 0  # 변수 초기화

# while True:  => 무한반복(조심해서 써야함!)  컨트롤 C를 두번누르면 종료
while hit < 1001:
    hit += 1 # hit를 1씩 증가

    print(f'나무를 {hit}번 찍었습니다.')
    if hit == 10:
        print(f'나무가 {hit}번 찍어 넘어갔습니다!!')
        break
    else:
        print('나무가 아직 넘어가지 않았습니다!!')

print('나무찍기 완료!')
