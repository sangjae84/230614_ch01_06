# 문자열 서식

# 데이터 -> str(...) print(..., ..., ...)
# 파이썬 3.6 -> f-string (formatted string)

## f-string
'''
문자열 안에 변수의 값들을 삽입하기 위한 양식 -> 가독성, 편의성
'''
name = "박코딩"
age = 30
print("이름 :", name, "나이 :", age, "세")
print("이름 : " + name + " 나이 : " + str(age) + "세")
# f"" 혹은 f'' -> 이 안에 {변수명}
print(f"이름 : {name} 나이 : {age}세")

l = ["아메리카노", "십센치", "권정열"]
print(f"내가 좋아하는 노래 : {l}") # f"" f'' -> {}로 표시한다

f = 0.123913912389  # 소수점 -> 소수점 밑의 2자리.
print(f'{f:.2f}') # f:.표시하고싶은자리수f
print(f'{f:.4f}') # f:.표시하고싶은자리수f
# https://blockdmask.tistory.com/429

# format 메소드 -> 변수에 사용하기에 편하게.
# 서식 지정자 -> c, c++, java, printf