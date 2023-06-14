# 문자열

## 문자열 조작하기

### 문자열 바꾸기

'''
문자열.replace('바꿀문자열','새문자열') -> 기존 문자열 안의 바꿀 문자열을 새 문자열로 '교체'
-> 매번 사본이 나옴.
'''
greeting = "안녕하세요! 김파이썬씨"
print(greeting)
print(greeting.replace("파이썬", "코딩"))
print(greeting)
new_greeting = greeting.replace("파이썬", "코딩")
print(new_greeting)

### 문자열 분리하기
### 문자열.split(구분자) -> 구분자를 기준으로 문자열을 리스트화 (구분자를 입력 안하면 -> " "(공백))
a = "태조 정종 태종 세종 문종 단종 세조"
print(a.split(), a.split(" "), a.split("종")) # '' <- 빈 구분자 이런건 X
print(list(a))  # 문자열 -> 리스트 (한 글자씩 조개져서 표현)
# map(int, input().split()) # -> 요소요소마다 int를 적용 -> split을 통해서 공백으로 나눠줘서...
a = "태조,정종,태종,세종,문종,단종,세조"
print(a.split(","))

# 문자열 리스트 연결하기 (특정한 구분자를 입력)
b = ['태조', '정종', '태종', '세종', '문종', '단종', '세조']
# b.join(...) -> 이런 메소드가 없음?
print("".join(b)) # 합칠 경우, 요소들 사이에 들어갈 '구분자'에다가 join(시퀀스)
print(",".join(b))
print(";".join(b))
print(" ".join(b)) # -> join 빈("")게 가능. / split -> 빈("") 안 됨.

# 일괄 대문자화, 소문자화
t = "Hello, Python!"
print(t.upper()) # uppercase
print(t.lower()) # lowercase
u = "HELLO! PYTHON"
l = "hello! python"
print(t.isupper())
print(u.isupper())
print(l.isupper())
print(t.islower())
print(u.islower())
print(l.islower())

# 채우기 및 삭제
text = "                앞 뒤로 스페이스가 있는 경우               "
print(text)
print(text.replace(" ", ""))
print(text.strip())
print(text.lstrip()) # left
print(text.rstrip()) # right
d = "614" # 4자리를 맞춰줘야함. -> 0.
print("0" + d)
d2 = "64"
print("00" + d2)
# 문자열.rjust(N, S) : N은 정렬의 기준이 되는 길이. S:채우는데 쓰이는 문자.
print(d2.rjust(4, "0")) # justify -> right
print(d2.rjust(4, "I")) # justify -> right
print(d2.rjust(4, " ")) # justify -> right
# 문자열.ljust(N, S)
print(d2.ljust(4, "0")) # justify
# 문자열 왼쪽에 길이를 만족시킬 때까지 0을 넣는...
print('d2.zfill(4)', d2.zfill(4)) # rjust(N, "0") # zero - fill
print('d2.zfill(6)', d2.zfill(6)) # rjust(N, "0") # zero - fill

### 메소드 체이닝
# -> 문자열을 변형시키는 메소드 -> 결과물 문자열 -> 자기 자신에게 계속 변화를 시킬 수 있음.
# 메소드를 줄줄이 연결한다고 해서 메소드 체이닝(method chaining)
t = "      hello world         "
print(t.strip())
print(t.strip().upper())
print(t.strip().upper().replace("WORLD", "EARTH"))
print(t.strip().upper().replace("WORLD", "EARTH").split()) # split() -> 리스트니까 안됨...
print(";".join(t.strip().upper().replace("WORLD", "EARTH").split()))
print(";".join(t.strip().upper().replace("WORLD", "EARTH").split()).lower())

# 문자열 위치 찾기 & 갯수 세기
# -> 리스트.index(...) => value의 인덱스를 찾음.
# -> 문자열.find(...) -> 텍스트 in 문자열 -> 한 글자가 아니더라도 부분문자열을 찾을 수 있게
t = "아메리카노"
print(t.find("메")) # 인덱스 개념
print(list(t).index("메"))
print(t.find("리카")) # -> find를 사용해줘야 한다
# print(list(t).index("리카"))  # ValueError: '리카' is not in list
t2 = "리카리카리카"
print(t2.find("리카"))  # 맨 앞쪽.

## 문자열 개수 세기
print(t2.count("카"))
print("찐찐찐찐찐이야 완전 찐이야".count("찐"))