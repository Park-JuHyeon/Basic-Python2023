# 복합형

a1 = 1
a2 = 2
a3 = 3
a4 = 4
a5 = 5
a6 = 6
a7 = 7
a8 = 8
a9 = 9
a10 = 10

print(a1 + a2 + a3 + a4 + a5 + a6 +a7 + a8 +a9+a10)

# 리스트 == 배열
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)
sum = 0
for i in arr:
    sum += i
print(sum)

arr1 = [1,2.3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello', 13 , 'World!', True]
print(arr3)
print(type(arr3))
#print('arr1의 2번 인덱스 값' + str(arr1[2]))

arr4 = [] # 빈 리스트
arr5 = list()
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]] # 3차원 배열 == 대괄호의 개수
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]] # 2차원 배열
print(arr7)

## 튜플 = 배열이지만 수정 및 추가 아무것도 불가능함.
tuple1 = (1,2,3,4)
print(tuple1)

arr5.append(4)
print(arr5)

# tuple1.append(4)
print(tuple1)
print(type(tuple1))

# 딕셔너리 - 사전처럼 등록한 정보를 한번에 나오게 해줌, "구조를 잘 봐둘것!!"
spiderman = {'name' : 'Peter Parker', 
              'age' : 18,
           'weapon' : 'Web shooter',
         'deserter' : '탈영병'}

print(spiderman)
print(spiderman['weapon'])
print(spiderman['deserter'])
print(type(spiderman))

# 집합
set1 = set([1,2,3,4])   # 
print(set1)

set1 = set("Hello world")
print(set1)



