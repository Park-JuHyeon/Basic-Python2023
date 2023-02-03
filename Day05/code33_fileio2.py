# 파일 읽어오기

file = open('./Day05/sample05.txt','r',encoding='utf-8')

while True:
    text = file.read()
    if not text: break
    else:
        print(text)

file.close()  # 파일을 오픈했으면 반드시 클로즈를 해줘야한다.



