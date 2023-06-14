# 리스트 응용

## 리스트 조작하기

### 리스트에 요소 추가하기

'''
* append : 요소 하나를 추가 (맨 뒤에)
* extend : 리스트를 연결하여 확장
* insert : 특정한 인덱스에 요소를 추가
'''
from builtins import reversed

### 기존 리스트에 요소 하나 추가하기

a = [10, 20, 30]
print(a)
# a = [10, 20, 30, 500] # 재할당 (다시 대입하지 않아도...)
a.append(500) # append : 리스트 맨 뒷자리에 새로운 원소(요소)를 추가
# ? : 없던 인덱스에는 값을 할당할 수 X -> append를 사용하게 되면 신규 인덱스를 생성 및 값 할당
# '리스트'라는 자료형, 타입, 클래스에 딸린 내장 기능 = 메소드.
print(a)

# b = []
b = list()
print(b)
b.append(10)
print(b)

### 리스트 안에 리스트 추가하기
l = [[0] * 5] * 5 # 행 -> 열
print(l, len(l))
l.append([1])
print(l, len(l))  # append 시에 길이는 무조건 1씩 증가

### 리스트 확장하기
a = ["사과"]
b = ["배"]
print(a + b)
a = ["사과"] * 3
print(a)
a.extend(b)  # append, extend -> 다시 할당/대입 과정?
# inplace -> 대체 -> 메소드를 실행하는 순간 굳이 재대입/재할당 -> 원래 변수에 영향을 미친다
print(a)
print(a + b)
print(a + b)
print(a + b)
print(a + b)
print(a) # a는 변하지 않는다! (연산자로 하면) *, + 똑같은데...
# append, extend? -> 원본에 영향을 미친다 (할당연산자 없이 쓰는 애들)
# extend  => + 가 아니라 += 의 역할을 한다
# extend는 전달받은 리스트의 원소를 하나씩 반복하면서 append라고 보시면 됨.
l = [1, 2 ,3]
l2 = [4, 5, 6]

#1.
l3 = l + l2
print("#1", l3)

#2.
l3 = []
l3.extend(l)
l3.extend(l2)
print("#2", l3)

#3.
l3 = []
for v1 in l:
    l3.append(v1) # 2배씩으로 만들어서 더해야한다
for v2 in l2:
    l3.append(v2)
print("#3", l3)

#3-1.
l3 = []
for v1 in l:
    # break? continue?
    l3.append(v1 * 2) # 2배씩으로 만들어서 더해야한다
for v2 in l2:
    l3.append(v2 * 2)
print("#3", l3)

### 리스트의 특정 인덱스에 요소 추가하기
# 리스트객체.insert(인덱스, 요소)는 리스트의 특정 인덱스에 요소 하나를 추가합니다.
a = list(range(10, 40, 10))
print(a)  # [10, 20, 30]
# a.insert(2, 15)  # 인덱스 2번째
a.insert(1, 15)  # 순서상 2번째 자리
print(a)
'''
* insert(0, 요소): 리스트의 맨 처음에 요소를 추가
* insert(len(리스트), 요소): 리스트 끝에 요소를 추가
'''
a.insert(0, 5)  # 파이썬 상 속도를 많이 잡아먹음 -> stack, queue, deque. (자료구조)
# index 바탕으로 어느 지점에 값을 넣어줘야하나 '찾는 로직' => 느린 메소드.
a.insert(len(a), 100)  # 굳이 할 필요가 없다
# a.append(100)
print(a)


### 리스트에서 요소 삭제하기
print("삭제 전", a)
del a[0]
print("삭제 후", a)
store = [10000, 2000, 5162]
# 가장 마지막 결제한 금액을 확인해서 print하고, 해당 값을 (리스트에서) 삭제
print(store)
print(store[-1])
del store[-1]
print(store)

# 리스트에서 특정 인덱스 값을 찾아서 삭제 -> 반환

store = [10000, 2000, 5162]
# 가장 마지막 결제한 금액을 확인해서 print하고, 해당 값을 (리스트에서) 삭제
print(store)
# print(store[-1])
# del store[-1]
# pop()은 리스트의 마지막 요소를 삭제한 뒤 삭제한 요소를 반환
p = store.pop() # pop(-1), pop(len(..)-1)
print(p)
print(store)

store = [10000, 2000, 5162]
print(store)
p = store.pop(0)  # 인덱스 -> 인덱스 번째의 값을 반환하고, 해당 값을 리스트에서 삭제
# 리스트객체.pop(인덱스) : 해당 인덱스의 값을 꺼내옴. (인덱스가 없으면 -1로 default)
print(p)
print(store)

# pop: 마지막 요소 또는 특정 인덱스의 요소를 삭제

# 리스트에서 특정 값을 찾아서 삭제
cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '레드벨벳 쿠키']
print(cookies)
# r = cookies.remove("치즈 쿠키")  # pop 처럼 삭제된 결과 X
# print(r)
cookies.remove("치즈 쿠키")  # pop 처럼 삭제된 결과 X
# 특정한 값을 찾는 기능.
print(cookies)
# 리스트.remove(값) -> 해당 값의 요소를 삭제

print(cookies.index("오레오 쿠키"))
# 리스트.index(값) -> 해당 값의 요소의 인덱스를 반환)
# idx = cookies.index("오레오 쿠키")
# del cookies[idx]
cookies.remove("오레오 쿠키")
print(cookies)

cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '마카다미아 쿠키', '레드벨벳 쿠키', '마카다미아 쿠키']
# index 혹은 remove 사용했을 때, 무엇을 검색 또는 삭제해줄까요?
print("cookies.index(\"마카다미아 쿠키\")", cookies.index("마카다미아 쿠키")) # 1개만 나옴
# 가장 먼저 발견되는 1개. (index 0부터해서...)

index = 0
value = "마카다미아 쿠키"
# for c in cookies:
# for i, c in enumerate(cookies):
for i in range(len(cookies)):
    # if c == value:
    if cookies[i] == value:
        # del(delete) ... -> remove
        break
    # index += 1
# print(index)
print(i)

print(cookies)
# print(cookies.index("초코파이")) # ValueError: '초코파이' is not in list
print("초코파이" in cookies)
# cookies.remove("초코파이") # list.remove(x): x not in list

store = ["마제소바", "토리동", "부타동"]
# while store:  # 리스트 -> False? -> 그 안에 요소가 없을 때...
# while True:
#     print(store)
#     order = input("무엇을 주문하시겠습니까? : ")
#     if order in store:
#         store.remove(order)  # 요소를 계속 제거...
#         print(order + "을(를) 드리겠습니다")
#     else:
#         print(order + "은(는) 현재 없는 메뉴입니다")
#     if len(store) == 0: # if not store:
#         break
# print("장사 끝났습니다")


### 특정 값의 개수 구하기
cookies = ['마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '치즈 쿠키', '레드벨벳 쿠키', '치즈 쿠키']
# 쿠키의 개수
print('cookies.count("치즈 쿠키")', cookies.count("치즈 쿠키"))  # 정확하게 일치하는지
song = "'마카다미아 쿠키', '치즈 쿠키', '오레오 쿠키', '치즈 쿠키', '레드벨벳 쿠키', '치즈 쿠키'"
print(song.count("쿠키"))  # 문자열(string) -> 특정한 단어가 몇 개 존재하는지?

### 리스트의 뒤집기
print(cookies)
print(cookies[::-1])  # 슬라이스 음수 증가폭
print(list(reversed(cookies)))  # reversed
print(cookies)  # 원본에 반영이 안됨 (뒤집었다는 것)
cookies.reverse()  # 리스트객체.reverse()
print("cookies.reverse() :", cookies)
print(cookies)

### 리스트의 요소 정렬
'''
sort()는 리스트의 요소을 작은 순서대로 정렬합니다(오름차순).

sort() 또는 sort(reverse=False): 리스트의 값을 작은 순서대로 정렬(오름차순)
sort(reverse=True): 리스트의 값을 큰 순서대로 정렬(내림차순)
'''
import random
r_number = random.choices(range(1000), k=10)
print(r_number)
print(sorted(r_number))  # reversed -> 뒤집어진, sorted -> 정렬된
print("<오름차순>")
for r in sorted(r_number):
    print(r)
# 오르막 -> 오름차순. (ascending) - asc (데이터가 등장 혹은 전개되는 방향)
# 1, 2, 3....
# 내리막 -> 내림차순  (descending) - desc
# 100, 99, 98, ...
print(sorted(r_number)[::-1])
print(sorted(r_number, reverse=True))  # sorted 정렬 -> 오름차순 -> 뒤집겠니?
print(list(reversed(sorted(r_number)))) # reversed -> print -> list를 묶어줘야함
# reversed(함수) & 리스트.reverse()
# sorted(함수) & 리스트.sort()
r_number = random.choices(range(1000), k=10)
print("r_number", r_number)
r_number.sort()
print("r_number.sort()", r_number)  # 오름차순

r_number = random.choices(range(1000), k=10)
print("r_number", r_number)
r_number.sort(reverse=True)
print("r_number.sort(reverse=True)", r_number)  # 내림차순

### 리스트의 모든 요소 삭제
print("cookies", cookies)
cookies.clear()
print("cookies", cookies)

### 리스트의 할당과 복사
'''
어떠한 값을 새로운 곳에 복사하는 방법
1. 할당 (assignment)
2. 얕은 복사 (shallow copy)
3. 깊은 복사 (deep copy)
'''
a = [0] * 5
print("a", a)
b = a  # b에 a를 '할당'
print("b", b)
a[0] = 100
a[1] = 150
print("b", b)
print(a is b)  # 2개가 같습니까?
c = a[:]  # 슬라이스로 복사한 경우에는 할당이 아니라 '얕은 복사'이므로 서로 영향을 미치지 X
print(a is c)  # 2개의 주소가 같습니까?
a[0] = 1200
a[1] = 100
a[2] = 50
print(c)
d = a.copy() # 얕은 복사.
print(c is d)

e = [a, b, c] # 리스트를 담은 리스트.
f = e.copy() # e[:] -> 얕은 복사
print("e is f :", e is f)
print(f)
a[0] = 1338
print(f)

import copy  # copy
g = copy.deepcopy(e)
print("g", g)
a[0] = 21381238
print("g", g)

# 1. 할당 - 얕은 복사 : 할당 -> 특정한 데이터를 저장한 주소를 넘기는 것.
# 2. 얕은 복사 -> 같은 데이터지만, 다른 주소를 가지도록 사본을 만드는
# (내부에 들어있는 주소까지 연결을 끊어주진않아요)
# 3. 깊은 복사 (import copy.deepcopy) -> 모든 주소들의 연결을 끊어버려서 사본을 만드는 것.

# 리스트(튜플) 가장 작은 수, 가장 큰 수, 합계
# 가장 작은 수, 가장 큰 수

# 1. 정렬
a = random.choices(range(1, 1000), k=4)
print("a", a)
a.sort()
print("a", a)
print("최소값", a[0])
print("최대값", a[-1])

# 2. 반복 -> 모든 요소 중에 가장 크거나, 작은 값... 비교
b = random.choices(range(1, 1000), k=10)  # 이중에 가장 큰 값을 구하세요 (sort 쓰지 않고)
n = 0  # 외부에 저장된 값
for v in b:
    print("n:", n, "v:", v)
    # 최대값을 구하는 방법
    # if n < v:
    #     n = v  # 더 큰 값을 n에 대입해서...
    # 최소값...
    if n == 0 or n > v:
        n = v
# 전체 반복을 끝내고 나면...
print(b, n)

# 3. 함수.
# 최대값 : maximum -> max
# 최소값 : minimum -> min
print(max(b))
print(min(b))

# 합계
s = 0
for i in range(1, 10): # 1 ~ 9.
    s += i
print(s)
# summarization -> sum
print(sum(range(1, 10)))
print(sum([329382, 129312328, 1231231]))

s = ["바나나", "알러지", "원숭이"]
# sum(s) # unsupported operand type(s) for +: 'int' and 'str' -> 0?
# 문자열들은 sum을 쓸 수 X.
c = ""
for a in s: # 1 ~ 9.
    c += a
print(c)

# 리스트 표현식 (리스트 컴프리헨션 - list comprehension)
## -> 리스트 안에 for 반복문과 if 조건문으로 -> 값들의 묶음을 표현.
## -> 리스트 안에 식, for 반복문, if 조건문 등을 지정하여 리스트를 생성 = 리스트 컴프리헨션
## [식 for 변수 in 시퀀스]

a = []
for i in range(10):
    a.append(i ** 2)
print(a)
a = [i ** 2 for i in range(10)]
print(a)
a = [i ** 0.5 for i in range(5, 10, 2)]
print(a)
a = [k ** 3.5 for k in range(3, 12, 3)]
print(a)
b = ["아메리카노", "카푸치노", "프라푸치노"]
# c = []  # 맨 끝 2자리 옮기기
# for v in b:
#     c.append(v[-2:])
# print(c)
# c = [v[-2:] for v in b]
c = [v + " 나왔습니다!" for v in b]
print(c)


# 리스트 컴프리헨션 + if 조건문
'''
[식 for 변수명 in 리스트 if 조건식]  # if 조건식을 만족시키는 값만, 식으로 표현
'''
d = []
for v in b:
    # print(v)
    if "푸" in v:
        # print(v)
        d.append(v)
print("d", d)
e = [v for v in b if "푸" in v]
print("e", e)

# 조건부 표현식 (삼항연산자) -> for 앞에 (식)
e = ["나 단 거 좋아해" if v == "프라푸치노" else "나 단 거 싫어해" for v in b if "푸" in v]
print("e", e)
# 리스트 컴프리헨션의 if문은 -> 만족을 안 시키면 필터링. -> continue -> len이 바뀜 !!!!
# else가 없음...
# 조건부 표현식(삼항연산자)는 조건의 T/F와는 상관없이 각 행이 여전히 존재. => 값. -> len 안바뀜
# else가 있음...

# 이중 for문
for i in range(10): # i <- 안 겹치게만.
    for j in range(10):  # 시퀀스에서 값을 빼내올 때 쓰는 변수명이 안겹치게만 조심. j
        print(i, j, i * j)
        # 삼중... 사중...
# 이중 for문? 이중 리스트 컴프리헨션
print([(i, j, i * j) for j in range(0, 10, 2) for i in range(0, 10, 3)])