# 딕셔너리 응용

## 딕셔너리 조작

x = {
    'a': 10, 'b': 20, 'c': 30, 'd': 40,
}
print(x)
x['a'] = 100
print(x)
x['e'] = 70
print(x)

# 객체.메소드(...)
x.update(a=1000)  # 변수로 만들 수 있는 키 이름.
x.update(f=1000)  # 변수로 만들 수 있는 키 이름.
print(x)
# 2개 이상의 키를 넣을 수 있음
# x[키] <- 한 번에 하나만
x.update(a=50, b=70, c=90)  # 2개 이상의 키를 업데이트.
print(x) # 키가 변수화할 수 있는 문자열. (숫자, Boolean, 특수문자가 혼합된 문자열...)
# x.update(1=50)
x[1] = 50
print(x)  # x[키] -> 할당 -> 키 -> 제약조건이 리스트, 딕셔너리만 아니면 됨
# x.update(...) -> 다중 업데이트가 가능, 키의 조건이 까다로움.

# 딕셔너리 키-값 쌍의 삭제
print(x)
del x['a']  # del
print(x)
# print(x.pop()) # 딕셔너리는 순서가 없어서 pop() <- 기본값 처리 X
print(x.pop('b')) # 키와 함께... -> pop은 반환값
print(x)
# print(x.pop('hello')) # KeyError: 'hello'
print(x.pop('hello', 0)) # 만약에 해당 삭제대상의 key가 없다면...
# 딕셔너리.pop(키, 기본값)

# 전체 삭제
print(x)
x.clear()
print(x)

# get을 통한 값 가져오기
x = {
    'a': 10, 'b': 20, 'c': 30, 'd': 40,
}
# print(x['e'])  # KeyError: 'e'
if 'e' in x:
    print(x['e'])
print(x.get("a")) # 있는 키
print(x.get("e")) # 없는 키 -> None (오류가 안 난다)
print(x.get("e", 0)) # 없을 경우에 반환해줄 '기본값'
# 딕셔너리.get(키, 기본값=None)


# 딕셔너리 키-값-아이템
for i in x:
    print(i)  # i -> key
    # 시퀀스 취급해서 반복 -> key
# for문 반복시 요소로는 key.

print(x.keys()) # 딕셔너리의 key 목록을 받는 메소드
print(x.values()) # 딕셔너리의 value 목록을 받는 메소드
print(x.items()) # 딕셔너리의 key, value 쌍을 받는 메소드
for i in x.items():
    print(i)
for k, v in x.items(): # 언패킹
    # print(k)
    # print(v)
    print(f"키 : {k}, 값 : {v}")


########## -> 계층형 딕셔너리, 딕셔너리 얕은복사/깊은복사
a = {}
a['b'] = {}
a['b']['c'] = {} # "딕셔너리 안에 있는 딕셔너리를 '키'를 사용해서 호출."
"""
딕셔너리[키][키]
딕셔너리[키][키] = 값
"""
print(a)  # key에 못들어가고, value에는 딕셔너리 들어갈 수 있음
a['b']['a'] = 100
print(a)

b = a  # 할당
print(f"b is a : {b is a}")
a['b']['b'] = 100
print(b)

c = a.copy()
print(f"c is a : {c is a}")
a['b']['b'] = 1000
print(c)  # 주소값을 복사한 '얕은 복사'

import copy
d = copy.deepcopy(a)
print(f"d is a : {d is a}")
a['b']['b'] = 10000
print(a)
print(d)

# 고급 기술 : 리스트 컴프리헨션? -> 딕셔너리 컴프리헨션??? (있음)