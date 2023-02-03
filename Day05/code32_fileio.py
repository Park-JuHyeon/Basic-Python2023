# 글자 인코딩
# ASCII -> 한단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든나라 언어를 다 표현 가능

# 상대경로 == .(나) , ..(부모) 을 통해 어디로든 갈수있는 경로

# 파일 만들기
file = open('../sample07.txt', 'w', encoding='utf-8') # 파일을 쓰기로 만듬

file.write('안녕하세여~ \n')
file.write('와~ 두번째 파일이당~!\n')
file.write('절대경로에 파일이 생성될겁니다. \n')


file.close()

print('sample05.txt가 생성되었습니다.')



# 파일/폴더 경로



