# 외부 패키지를 사용
import requests

res = requests.get('https://www.naver.com')  # 네이버의 홈페이지 코드를 싹 가져와버리는 코드
print(res.status_code)
print('=====================')
print(res.content)




